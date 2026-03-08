import sys
sys.path.append(sys.path[0] + '/..')

from rsx.tools import *

raw = get('Datasets/sample.txt')
dna = list(fasta_strings(raw).values())[0]

min_length = 4
max_length = 12

rest_sites = []

for cur_length in range(min_length,max_length+1): #iter over dna with all possible lengths
    # print(cur_length)
    for i in range(len(dna)-cur_length+1):
        # print(i, dna[i:i+cur_length])
        possible_rs = reverse_complement(dna[i:i+cur_length])
        if possible_rs == dna[i:i+cur_length]:
            rest_sites.append([i+1, len(possible_rs)])

# print(rest_sites)

for i,x in rest_sites:
    print(i,x)
