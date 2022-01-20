import numpy as np
from typing import List


def get_noise_table() -> np.array:
    noise_array: List[str] = [
     "0.94373,0.048518,0.0051206,0.0013742,0.00054042,0.00026203,0.00014503,8.80E-05,5.70E-05,3.89E-05,2.77E-05,2.03E-05,1.53E-05,1.18E-05,9.28E-06,7.42E-06,6.02E-06,4.94E-06,4.11E-06,3.45E-06,2.92E-06,2.49E-06,2.14E-06,1.85E-06,1.62E-06,1.42E-06,1.25E-06,1.10E-06,9.80E-07,8.74E-07,7.83E-07,7.04E-07,6.35E-07,5.75E-07,5.22E-07,4.75E-07,4.75E-07,4.75E-07,0,0,0",
     "0.048518,0.94373,0.048518,0.0051206,0.0013742,0.00054042,0.00026203,0.00014503,8.80E-05,5.70E-05,3.89E-05,2.77E-05,2.03E-05,1.53E-05,1.18E-05,9.28E-06,7.42E-06,6.02E-06,4.94E-06,4.11E-06,3.45E-06,2.92E-06,2.49E-06,2.14E-06,1.85E-06,1.62E-06,1.42E-06,1.25E-06,1.10E-06,9.80E-07,8.74E-07,7.83E-07,7.04E-07,6.35E-07,5.75E-07,5.22E-07,4.75E-07,4.75E-07,4.75E-07,0,0",
     "0.0051206,0.048518,0.94373,0.048518,0.0051206,0.0013742,0.00054042,0.00026203,0.00014503,8.80E-05,5.70E-05,3.89E-05,2.77E-05,2.03E-05,1.53E-05,1.18E-05,9.28E-06,7.42E-06,6.02E-06,4.94E-06,4.11E-06,3.45E-06,2.92E-06,2.49E-06,2.14E-06,1.85E-06,1.62E-06,1.42E-06,1.25E-06,1.10E-06,9.80E-07,8.74E-07,7.83E-07,7.04E-07,6.35E-07,5.75E-07,5.22E-07,4.75E-07,4.75E-07,4.75E-07,0",
     "0.0013742,0.0051206,0.048518,0.94373,0.048518,0.0051206,0.0013742,0.00054042,0.00026203,0.00014503,8.80E-05,5.70E-05,3.89E-05,2.77E-05,2.03E-05,1.53E-05,1.18E-05,9.28E-06,7.42E-06,6.02E-06,4.94E-06,4.11E-06,3.45E-06,2.92E-06,2.49E-06,2.14E-06,1.85E-06,1.62E-06,1.42E-06,1.25E-06,1.10E-06,9.80E-07,8.74E-07,7.83E-07,7.04E-07,6.35E-07,5.75E-07,5.22E-07,4.75E-07,4.75E-07,4.75E-07",
     "0.00054042,0.0013742,0.0051206,0.048518,0.94373,0.048518,0.0051206,0.0013742,0.00054042,0.00026203,0.00014503,8.80E-05,5.70E-05,3.89E-05,2.77E-05,2.03E-05,1.53E-05,1.18E-05,9.28E-06,7.42E-06,6.02E-06,4.94E-06,4.11E-06,3.45E-06,2.92E-06,2.49E-06,2.14E-06,1.85E-06,1.62E-06,1.42E-06,1.25E-06,1.10E-06,9.80E-07,8.74E-07,7.83E-07,7.04E-07,6.35E-07,5.75E-07,5.22E-07,4.75E-07,4.75E-07",
     "0.00026203,0.00054042,0.0013742,0.0051206,0.048518,0.94373,0.048518,0.0051206,0.0013742,0.00054042,0.00026203,0.00014503,8.80E-05,5.70E-05,3.89E-05,2.77E-05,2.03E-05,1.53E-05,1.18E-05,9.28E-06,7.42E-06,6.02E-06,4.94E-06,4.11E-06,3.45E-06,2.92E-06,2.49E-06,2.14E-06,1.85E-06,1.62E-06,1.42E-06,1.25E-06,1.10E-06,9.80E-07,8.74E-07,7.83E-07,7.04E-07,6.35E-07,5.75E-07,5.22E-07,4.75E-07",
     "0.0001142,0.00020356,0.00041294,0.0010279,0.0037165,0.035022,0.9258,0.03345,0.0037165,0.0010279,0.00041294,0.00020356,0.0001142,7.01E-05,4.59E-05,3.16E-05,2.26E-05,1.67E-05,1.27E-05,9.85E-06,7.78E-06,6.26E-06,5.10E-06,4.21E-06,3.51E-06,2.96E-06,2.51E-06,2.15E-06,1.86E-06,1.61E-06,1.41E-06,1.24E-06,1.09E-06,9.71E-07,8.65E-07,7.74E-07,6.95E-07,6.26E-07,5.66E-07,5.14E-07,4.67E-07",
     "8.37E-05,0.00013485,0.00023713,0.00047316,0.0011529,0.015303,0.035891,0.90787,0.034582,0.0040451,0.0011529,0.00047316,0.00023713,0.00013485,8.37E-05,5.53E-05,3.84E-05,2.77E-05,2.07E-05,1.58E-05,1.23E-05,9.79E-06,7.91E-06,6.47E-06,5.37E-06,4.50E-06,3.80E-06,3.24E-06,2.79E-06,2.42E-06,2.11E-06,1.85E-06,1.63E-06,1.44E-06,1.28E-06,1.14E-06,1.03E-06,9.25E-07,8.35E-07,7.57E-07,6.88E-07",
     "5.40E-05,8.09E-05,0.00012883,0.0002235,0.00043863,0.035514,0.010078,0.029835,0.88994,0.028925,0.0035619,0.0010462,0.00043863,0.0002235,0.00012883,8.09E-05,5.40E-05,3.78E-05,2.75E-05,2.06E-05,1.59E-05,1.25E-05,9.96E-06,8.08E-06,6.65E-06,5.54E-06,4.66E-06,3.96E-06,3.39E-06,2.92E-06,2.54E-06,2.22E-06,1.95E-06,1.73E-06,1.53E-06,1.37E-06,1.23E-06,1.10E-06,9.95E-07,9.02E-07,8.19E-07",
     "0,0,0,0,0,0.064361,0.014003,0.0058096,0.020095,0.87201,0.01957,0.002537,0.00076791,0.0003289,0.00017038,9.96E-05,6.32E-05,4.26E-05,3.01E-05,2.21E-05,1.67E-05,1.29E-05,1.02E-05,8.19E-06,6.69E-06,5.53E-06,4.62E-06,3.91E-06,3.33E-06,2.86E-06,2.48E-06,2.16E-06,1.90E-06,1.67E-06,1.48E-06,1.32E-06,1.18E-06,1.06E-06,9.58E-07,8.67E-07,7.87E-07",
     "0,0,0,0,0,0.086373,0.021334,0.005884,0.0034449,0.013128,0.85408,0.012827,0.0017506,0.00054606,0.00023892,0.00012584,7.45E-05,4.79E-05,3.26E-05,2.32E-05,1.72E-05,1.31E-05,1.02E-05,8.08E-06,6.53E-06,5.36E-06,4.45E-06,3.74E-06,3.17E-06,2.72E-06,2.34E-06,2.04E-06,1.78E-06,1.57E-06,1.39E-06,1.23E-06,1.10E-06,9.90E-07,8.91E-07,8.06E-07,7.31E-07",
     "0,0,0,0,0,0.10023,0.028875,0.0085286,0.0029699,0.0023399,0.0094166,0.83615,0.0092227,0.0013251,0.00042597,0.0001904,0.00010196,6.12E-05,3.98E-05,2.74E-05,1.97E-05,1.46E-05,1.12E-05,8.79E-06,7.03E-06,5.71E-06,4.71E-06,3.93E-06,3.32E-06,2.83E-06,2.43E-06,2.10E-06,1.84E-06,1.61E-06,1.42E-06,1.26E-06,1.13E-06,1.01E-06,9.09E-07,8.21E-07,7.44E-07",
     "0,0,0,0,0,0.10854,0.036063,0.01208,0.0042216,0.0018474,0.0018565,0.0076583,0.81822,0.0075143,0.0011366,0.00037653,0.00017193,9.36E-05,5.70E-05,3.74E-05,2.60E-05,1.89E-05,1.42E-05,1.09E-05,8.62E-06,6.93E-06,5.66E-06,4.69E-06,3.93E-06,3.33E-06,2.85E-06,2.46E-06,2.14E-06,1.88E-06,1.65E-06,1.46E-06,1.30E-06,1.17E-06,1.05E-06,9.45E-07,8.56E-07",
     "0,0,0,0,0,0.11313,0.042697,0.016172,0.0062176,0.0025542,0.0013912,0.0016906,0.0070031,0.80029,0.0068808,0.0010957,0.00037406,0.00017449,9.66E-05,5.96E-05,3.96E-05,2.78E-05,2.03E-05,1.54E-05,1.19E-05,9.49E-06,7.67E-06,6.30E-06,5.25E-06,4.42E-06,3.77E-06,3.24E-06,2.81E-06,2.45E-06,2.15E-06,1.90E-06,1.69E-06,1.51E-06,1.36E-06,1.22E-06,1.11E-06",
     "0,0,0,0,0,0.11494,0.048577,0.02057,0.0087699,0.003834,0.0018434,0.0012288,0.0017209,0.0070575,0.78236,0.0069414,0.0011637,0.0004094,0.00019509,0.00010979,6.86E-05,4.61E-05,3.27E-05,2.41E-05,1.84E-05,1.44E-05,1.15E-05,9.36E-06,7.73E-06,6.48E-06,5.48E-06,4.69E-06,4.05E-06,3.52E-06,3.09E-06,2.72E-06,2.41E-06,2.15E-06,1.93E-06,1.74E-06,1.57E-06",
     "0,0,0,0,0,0.11452,0.053495,0.025021,0.011748,0.0055827,0.0027578,0.0015448,0.0012307,0.0019082,0.0076708,0.76444,0.0075504,0.0013326,0.00048313,0.00023519,0.00013456,8.53E-05,5.80E-05,4.15E-05,3.09E-05,2.37E-05,1.87E-05,1.50E-05,1.23E-05,1.02E-05,8.61E-06,7.33E-06,6.30E-06,5.46E-06,4.77E-06,4.19E-06,3.71E-06,3.30E-06,2.95E-06,2.66E-06,2.40E-06",
     "0,0,0,0,0,0.11221,0.057268,0.029257,0.014985,0.0077285,0.0040638,0.0022584,0.0014634,0.0013547,0.0022526,0.0088148,0.74651,0.0086812,0.001613,0.00060265,0.00029971,0.00017434,0.00011198,7.70E-05,5.57E-05,4.18E-05,3.24E-05,2.57E-05,2.08E-05,1.71E-05,1.43E-05,1.21E-05,1.03E-05,8.93E-06,7.77E-06,6.82E-06,6.02E-06,5.35E-06,4.78E-06,4.29E-06,3.87E-06",
     "0,0,0,0,0,0.10826,0.059755,0.03301,0.01827,0.010159,0.005714,0.0033077,0.00206,0.0015271,0.0015954,0.0027766,0.010525,0.72858,0.010369,0.0020283,0.00078094,0.00039675,0.00023464,0.00015276,0.00010627,7.76E-05,5.88E-05,4.59E-05,3.67E-05,2.99E-05,2.48E-05,2.08E-05,1.77E-05,1.52E-05,1.32E-05,1.15E-05,1.01E-05,8.98E-06,8.00E-06,7.17E-06,6.46E-06",
     "0,0,0,0,0,0.10291,0.060874,0.036037,0.021368,0.012715,0.0076241,0.0046519,0.0029536,0.0020509,0.0017134,0.0019654,0.003516,0.012863,0.71065,0.012676,0.0026104,0.0010358,0.00053756,0.00032322,0.0002133,0.00015009,0.0001107,8.46E-05,6.66E-05,5.36E-05,4.39E-05,3.66E-05,3.09E-05,2.64E-05,2.28E-05,1.99E-05,1.74E-05,1.54E-05,1.37E-05,1.23E-05,1.10E-05",
     "0,0,0,0,0,0.096375,0.060612,0.038148,0.024045,0.0152,0.0096641,0.0062177,0.0041,0.0028451,0.0021867,0.0020225,0.0024873,0.0045129,0.015893,0.69272,0.015664,0.0033959,0.0013886,0.00073622,0.00045005,0.00030104,0.00021427,0.00015961,0.00012309,9.76E-05,7.91E-05,6.53E-05,5.47E-05,4.65E-05,3.99E-05,3.46E-05,3.03E-05,2.67E-05,2.37E-05,2.12E-05,1.90E-05",
     "0,0,0,0,0,0.088913,0.059034,0.039227,0.026102,0.017413,0.011671,0.0078928,0.0054287,0.0038567,0.0029122,0.0024526,0.002465,0.003187,0.0058071,0.019648,0.67479,0.019365,0.0044198,0.0018624,0.0010088,0.00062695,0.00042508,0.00030604,0.00023023,0.00017912,0.00014309,0.00011679,9.70E-05,8.18E-05,6.98E-05,6.03E-05,5.25E-05,4.62E-05,4.09E-05,3.64E-05,3.27E-05",
     "0,0,0,0,0,0.080802,0.056287,0.039243,0.027398,0.019175,0.013475,0.0095379,0.0068375,0.0050132,0.0038245,0.0031231,0.0028472,0.003055,0.0040879,0.0074261,0.024104,0.65686,0.023755,0.0057078,0.0024786,0.0013715,0.00086661,0.00059556,0.00043372,0.00032954,0.00025863,0.00020823,0.00017115,0.0001431,0.00012138,0.00010421,9.04E-05,7.92E-05,6.99E-05,6.21E-05,5.56E-05",
     "0,0,0,0,0,0.072352,0.052592,0.038264,0.02788,0.020362,0.014927,0.011011,0.0082059,0.0062197,0.0048478,0.0039541,0.003464,0.0033738,0.0038039,0.0052044,0.0093753,0.02916,0.63893,0.028733,0.0072683,0.0032527,0.0018386,0.0011811,0.00082278,0.00060608,0.00046508,0.00036821,0.00029878,0.00024733,0.00020813,0.00017758,0.00015331,0.00013371,0.00011765,0.00010432,9.31E-05",
     "0,0,0,0,0,0.063885,0.048225,0.036442,0.02758,0.020922,0.015929,0.012196,0.0094185,0.0073727,0.0058939,0.0048669,0.00422,0.0039285,0.0040345,0.0047166,0.0065371,0.01163,0.034633,0.621,0.034119,0.009086,0.0041902,0.0024196,0.0015804,0.0011159,0.00083143,0.00064436,0.00051462,0.00042086,0.00035086,0.00029716,0.00025506,0.00022141,0.00019409,0.0001716,0.00015284",
     "0,0,0,0,0,0.055705,0.043487,0.033989,0.026609,0.020882,0.016446,0.01302,0.010387,0.008381,0.006876,0.0057809,0.0050345,0.0046077,0.0045117,0.0048274,0.0057884,0.0080696,0.014136,0.040275,0.60307,0.039665,0.01112,0.005285,0.0031176,0.0020703,0.0014817,0.0011167,0.00087404,0.00070418,0.00058041,0.0004873,0.0004154,0.00035866,0.00031307,0.00027585,0.00024504",
     "0,0,0,0,0,0.048069,0.038667,0.031145,0.025133,0.020332,0.016507,0.013468,0.011066,0.0091822,0.0077249,0.0066255,0.0058361,0.0053301,0.0051075,0.0052078,0.0057451,0.0070048,0.0097699,0.016813,0.045804,0.58515,0.045094,0.013309,0.0065185,0.0039282,0.0026521,0.0019239,0.0014667,0.0011594,0.00094229,0.00078276,0.00066185,0.00056785,0.00049321,0.00043288,0.00038337",
     "0,0,0,0,0,0.04116,0.03401,0.028144,0.023337,0.019402,0.016189,0.013573,0.011454,0.0097515,0.0084002,0.0073512,0.0065692,0.0060334,0.0057406,0.0057117,0.0060088,0.006775,0.008343,0.011594,0.019565,0.050947,0.56722,0.050135,0.015578,0.0078627,0.0048405,0.0033225,0.0024431,0.0018839,0.001504,0.0012331,0.0010324,0.0008791,0.00075913,0.00066328,0.00058536",
     "0,0,0,0,0,0.035086,0.029699,0.025182,0.021399,0.018235,0.015596,0.013402,0.011588,0.010099,0.0088929,0.0079349,0.0072008,0.006676,0.0063572,0.0062573,0.0064131,0.0069051,0.0079011,0.0097755,0.013492,0.022295,0.055475,0.54929,0.054565,0.017849,0.009284,0.0058387,0.0040746,0.003037,0.0023687,0.00191,0.0015796,0.0013329,0.001143,0.00099344,0.00087318",
     "0,0,0,0,0,0.029878,0.025849,0.022406,0.019468,0.016965,0.014839,0.01304,0.011526,0.010262,0.0092206,0.0083789,0.007721,0.0072373,0.0069264,0.0067971,0.0068734,0.0072046,0.0078858,0.0091059,0.011273,0.015416,0.024917,0.059226,0.53136,0.058223,0.020051,0.010748,0.0069049,0.0048991,0.0037012,0.00292,0.0023779,0.0019839,0.0016871,0.0014571,0.0012746",
     "0,0,0,0,0,0.025511,0.022515,0.019912,0.017655,0.015702,0.014017,0.012571,0.011336,0.010291,0.009419,0.0087049,0.0081393,0.0077167,0.0074373,0.0073081,0.007346,0.0075836,0.0080794,0.0089404,0.010372,0.012808,0.017321,0.02736,0.062111,0.51343,0.061021,0.022123,0.012221,0.0080207,0.0057857,0.0044305,0.0035356,0.0029079,0.0024474,0.0020976,0.0018245",
     "0,0,0,0,0,0.021926,0.019706,0.017752,0.016034,0.014529,0.013214,0.012071,0.011085,0.010243,0.0095324,0.0089463,0.0084791,0.0081282,0.0078949,0.0077854,0.0078124,0.0079988,0.0083832,0.0090314,0.010059,0.011683,0.014355,0.01917,0.029572,0.064106,0.4955,0.06294,0.024023,0.013675,0.009169,0.0067245,0.0052195,0.0042131,0.0034996,0.0029712,0.0025666",
     "0,0,0,0,0,0.019041,0.017404,0.015946,0.01465,0.013502,0.012491,0.011604,0.010832,0.010169,0.0096066,0.0091418,0.0087715,0.0084954,0.0083155,0.0082374,0.0082712,0.0084338,0.008752,0.0092688,0.010055,0.011233,0.013026,0.015895,0.020935,0.031523,0.065245,0.47757,0.064011,0.025721,0.015089,0.010335,0.0077062,0.006063,0.0049502,0.0041528,0.0035568",
     "0,0,0,0,0,0.016776,0.015573,0.014492,0.013523,0.012659,0.011892,0.011216,0.010625,0.010116,0.009685,0.0093301,0.0090505,0.0088471,0.0087223,0.0086814,0.0087324,0.0088884,0.0091687,0.0096031,0.010238,0.011146,0.012454,0.01439,0.017412,0.022597,0.033196,0.065595,0.45964,0.064304,0.027202,0.016445,0.011507,0.0087232,0.0069565,0.0057451,0.0048676",
     "0,0,0,0,0,0.015051,0.014173,0.013378,0.012662,0.01202,0.011449,0.010944,0.010503,0.010124,0.0098063,0.0095481,0.0093502,0.009214,0.0091424,0.0091399,0.0092134,0.009373,0.0096333,0.010016,0.010551,0.011288,0.012302,0.013719,0.015766,0.018894,0.024143,0.03459,0.065249,0.44171,0.063912,0.028462,0.017732,0.012675,0.0097693,0.0078969,0.0065967",
     "0,0,0,0,0,0.013802,0.013166,0.012588,0.012067,0.011599,0.011183,0.010816,0.010498,0.010228,0.010005,0.0098299,0.0097034,0.0096273,0.0096044,0.0096389,0.0097364,0.009905,0.010156,0.010505,0.010974,0.011596,0.012419,0.01352,0.015022,0.017149,0.020335,0.025569,0.035716,0.064312,0.42378,0.062937,0.029507,0.018945,0.013834,0.01084,0.0088819",
     "0,0,0,0,0,0.012976,0.012521,0.012109,0.011738,0.011405,0.011112,0.010856,0.010637,0.010456,0.010313,0.010208,0.010142,0.010118,0.010138,0.010206,0.010327,0.010507,0.010754,0.011082,0.011505,0.012047,0.01274,0.013633,0.0148,0.016364,0.018536,0.021732,0.026875,0.03659,0.062891,0.40586,0.061486,0.030348,0.02008,0.014979,0.011933",
     "0,0,0,0,0,0.012536,0.012219,0.011933,0.011677,0.01145,0.011253,0.011086,0.010947,0.010838,0.01076,0.010713,0.010698,0.010718,0.010775,0.010872,0.011013,0.011204,0.011451,0.011764,0.012154,0.012638,0.013238,0.013988,0.014933,0.016146,0.017744,0.019928,0.023085,0.028066,0.037237,0.061092,0.38793,0.059666,0.031004,0.02114,0.01611",
     "0,0,0,0,0,0.012464,0.012251,0.012061,0.011894,0.01175,0.011628,0.01153,0.011456,0.011405,0.011379,0.011379,0.011406,0.011463,0.01155,0.011671,0.011829,0.012029,0.012276,0.012577,0.012942,0.013381,0.013913,0.014557,0.015346,0.016325,0.017563,0.019168,0.021329,0.024402,0.029156,0.03769,0.059022,0.37,0.05758,0.031499,0.022133",
     "0,0,0,0,0,0.01276,0.012626,0.01251,0.012412,0.012331,0.012269,0.012225,0.012201,0.012196,0.012212,0.01225,0.01231,0.012395,0.012506,0.012646,0.012818,0.013024,0.01327,0.013561,0.013904,0.014308,0.014784,0.015349,0.016023,0.016835,0.017829,0.019069,0.020655,0.022759,0.025704,0.030173,0.037998,0.056798,0.35207,0.055346,0.031874",
     "0,0,0,0,0,0.013466,0.013392,0.013331,0.013285,0.013254,0.013237,0.013236,0.01325,0.013281,0.013329,0.013396,0.013482,0.013589,0.013718,0.013871,0.014052,0.014262,0.014505,0.014785,0.015109,0.015482,0.015913,0.016414,0.016999,0.017687,0.018507,0.019498,0.020718,0.02226,0.024279,0.027058,0.031199,0.03827,0.054604,0.33414,0.053142",
     "0,0,0,0,0,0.014764,0.014734,0.014715,0.014709,0.014714,0.014731,0.014762,0.014806,0.014864,0.014937,0.015025,0.015131,0.015254,0.015396,0.01556,0.015746,0.015957,0.016197,0.016468,0.016775,0.017123,0.017518,0.017968,0.018485,0.019081,0.019775,0.020593,0.02157,0.02276,0.024246,0.026165,0.028768,0.032574,0.038916,0.053002,0.31621"
    ]
    return np.array([[float(val) for val in string_list.split(',')] for string_list in noise_array])
