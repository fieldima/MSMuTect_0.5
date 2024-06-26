# MSMuTect_0.5
Indel, Allele and mutation caller, specifically designed to call MS-stable vs MS-unstable pairs in tumors.

# Installation
git clone https://github.com/MaruvkaLab/MSMuTect_0.5  
cd MSMuTect_0.5  
pip3 install -r requirements.txt

# Usage
First, the loci file must be sorted properly:
This should work on all unix systems:   
sort -t $'\t' -k1,1 -k5n,5 -k4n,4 -V [original loci file] > [new loci file]    
Then: 
msmutect.sh [flags]  
For the most typical usage of calling microsatellite instability for a pair of BAMs:  
msmutect -T [tumorbam.bam] -N [normalbam.bam] -l [loci_file.phobos] -O [output_prefix] -c [number of cores to use] -m.  

If a run gets interrupted files with names like tmp_25147_1716098274.1160007_92669 will be left in the output directory. They can be deleted with no issue
# Publication
For orginal paper, see 
YE  Maruvka, Mouw K,  et al, Analysis of somatic microsatellite indels identifies driver events in human tumors
Called 0.5 (even though v3 was already made) since this version is intended for distribution, unlike prior versions which were for in house analysis only


# Authors
Dr. Yossi Maruvka, Avraham Kahan and the Maruvka Lab at Technion
For questions, suggestions, or concerns, open an issue or email k.avraham@technion.ac.il or yosi.maruvka@bfe.technion.ac.il

