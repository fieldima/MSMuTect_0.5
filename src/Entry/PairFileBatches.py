import numpy as np
from typing import List
from collections import namedtuple
from pysam import AlignmentFile

import src.Entry.FormatUtil
from src.IndelCalling.Locus import Locus
from src.IndelCalling.AlleleSet import AlleleSet
from src.IndelCalling.Histogram import Histogram
from src.IndelCalling.CallAlleles import calculate_alleles
from src.IndelCalling.CallMutations import call_mutations, is_possible_mutation, call_verified_locus
from src.IndelCalling.FisherTest import Fisher
from src.IndelCalling.MutationCall import MutationCall
from src.IndelCalling.AICs import AICs
from src.GenomicUtils.ReadsFetcher import ReadsFetcher
from src.GenomicUtils.LocusFile import LociManager
from . import BatchUtil

PairResults = namedtuple("PairResults", ['normal_alleles', 'tumor_alleles', 'decision'])


def format_full_mutations(normal_alleles: List[AlleleSet], tumor_alleles: List[AlleleSet], decisions: List[MutationCall]) -> List[List[str]]:
    normal_alleles_output = src.Entry.FormatUtil.format_alleles(normal_alleles)
    tumor_alleles_output = src.Entry.FormatUtil.format_alleles(tumor_alleles)
    mut_output_lines = format_mutated(decisions)
    return [normal_alleles_output, tumor_alleles_output, mut_output_lines]


def run_full_pair(normal: str, tumor: str, loci_file: str, batch_start: int,
                       batch_end: int, cores: int, flanking: int, output_prefix: str):
    loci_iterator = LociManager(loci_file, batch_start)
    noise_table = np.loadtxt(BatchUtil.get_noise_table_path(), delimiter=',')  # noise table
    results: List[List[str]] = BatchUtil.run_batch(partial_full_pair, [normal, tumor, flanking, noise_table], loci_iterator,
                                  (batch_end - batch_start), cores, BatchUtil.extract_NX3_results)
    allelic_header = f"{Locus.header()}\t{Histogram.header()}\t{AlleleSet.header()}\tMUTATION_CALL"
    BatchUtil.write_results(output_prefix + ".normal.all", results[0], allelic_header)
    BatchUtil.write_results(output_prefix + ".tumor.all", results[1], allelic_header)
    mutation_header = f"{Locus.header()}\t{Histogram.header(prefix='NORMAL_')}\t{AlleleSet.header(prefix='NORMAL_')}\t{Histogram.header(prefix='TUMOR_')}\t{AlleleSet.header(prefix='TUMOR_')}\t{MutationCall.header()}{AICs.header()}"
    BatchUtil.write_results(output_prefix + ".full.mut", results[2], mutation_header)


def get_allele_set(loci: List[Locus], BAM: str, flanking: int, noise_table) -> List[AlleleSet]:
    BAM_handle = AlignmentFile(BAM, "rb")
    reads_fetcher = ReadsFetcher(BAM_handle, loci[0].chromosome)
    allelic_results: List[AlleleSet] = []
    for locus in loci:
        current_histogram = Histogram(locus)
        reads = reads_fetcher.get_reads(locus.chromosome, locus.start - flanking, locus.end + flanking)
        current_histogram.add_reads(reads)
        current_alleles = calculate_alleles(current_histogram, noise_table)
        allelic_results.append(current_alleles)
    return allelic_results


def partial_full_pair(loci: List[Locus], normal: str, tumor: str, flanking: int, noise_table) -> List[List[str]]:
    if len(loci) == 0:
        return [[], [], []]
    normal_alleles: List[AlleleSet] = get_allele_set(loci, normal, flanking, noise_table)
    tumor_alleles: List[AlleleSet] = get_allele_set(loci, tumor, flanking, noise_table)
    fisher_calculator = Fisher()
    calls = [call_mutations(normal_alleles[i], tumor_alleles[i], noise_table, fisher_calculator) for i in range(len(normal_alleles))]
    return format_full_mutations(normal_alleles, tumor_alleles, calls)


def run_mutations_pair(normal: str, tumor: str, loci_file: str, batch_start: int,
                       batch_end: int, cores: int, flanking: int, output_prefix: str):
    loci_iterator = LociManager(loci_file, batch_start)
    noise_table = np.loadtxt(BatchUtil.get_noise_table_path(), delimiter=',')  # noise table
    results: List[str] = BatchUtil.run_batch(partial_mutations_pair, [normal, tumor, flanking, noise_table],
                                                     loci_iterator,
                                                     (batch_end - batch_start), cores)
    mutation_header = f"{Locus.header()}\t{Histogram.header(prefix='NORMAL_')}\t{AlleleSet.header(prefix='NORMAL_')}\t{Histogram.header(prefix='TUMOR_')}\t{AlleleSet.header(prefix='TUMOR_')}\t{MutationCall.header()}\t{AICs.header()}"
    BatchUtil.write_results(output_prefix + ".partial.mut", results, mutation_header)


def get_tumor_alleles(reads_fetcher: ReadsFetcher, locus: Locus, flanking: int, noise_table) -> AlleleSet:
    histogram = Histogram(locus)
    reads = reads_fetcher.get_reads(locus.chromosome, locus.start - flanking, locus.end + flanking)
    histogram.add_reads(reads)
    current_alleles = calculate_alleles(histogram, noise_table)
    return current_alleles


def partial_mutations_pair(loci: List[Locus], normal: str, tumor: str, flanking: int, noise_table) -> List[str]:
    if len(loci) == 0:
        return []
    normal_alleles: List[AlleleSet] = get_allele_set(loci, normal, flanking, noise_table)
    fisher_calculator = Fisher()
    possibly_mutated: List[MutationCall] = []
    tumor_reads_fetcher = ReadsFetcher(AlignmentFile(tumor), loci[0].chromosome)
    for current_normal_alleles in normal_alleles:
        if is_possible_mutation(current_normal_alleles):
            current_tumor_alleles = get_tumor_alleles(tumor_reads_fetcher, current_normal_alleles.histogram.locus, flanking, noise_table)
            possibly_mutated.append(call_verified_locus(current_normal_alleles, current_tumor_alleles, noise_table, fisher_calculator))
    return format_mutated(possibly_mutated)


def format_mutated(decisions: List[MutationCall]):
    mut_output_lines = [f"{str(decisions[i].normal_alleles.histogram.locus)}\t \
                    {str(decisions[i].tumor_alleles.histogram)}\t \
                    {str(decisions[i].tumor_alleles)}\t \
                    {str(decisions[i].normal_alleles.histogram)}\t \
                    {str(decisions[i].normal_alleles)}\t \
                    {str(decisions[i])}\t{str(decisions[i].aic_values)}" for i in range(len(decisions))]
    return mut_output_lines
