import sys
sys.path.append(sys.path[0] + '/..')

from rsx.proteins import *
import requests

raw_data = get('Datasets/rosalind_mprt.txt')

#formatting ID's into a tuple
raw_data = raw_data.split('\n')

#remove any blank entries
raw_data = list([x for x in raw_data if x != ''])

ID_table = []
for i, ID in enumerate(raw_data):
    ID_TRIM = ''
    for char in ID:
        if char == '_': break
        ID_TRIM += char
    ID_table.append(ID_TRIM)

ID_table = tuple(ID_table)
COMPLETE_ID_table = raw_data

# print(COMPLETE_ID_table)
# print(ID_table)

# making a http request to get fasta format data and store it in a tuple

fasta_table = tuple([uniprotget(id) for id in ID_table])

# finding N-glycosylation motifs -- N{P}[ST]{P}
# [ST] means either S or T, but no other
# {P} means anything but P

motif_table = []
for index,protein in enumerate(fasta_table):
    motif_table.append([COMPLETE_ID_table[index]])
    for i in range(len(protein)-3):
        aa = protein[i]
        N_glyc_check = aa == 'N' and protein[i+1] != 'P' and protein[i+2] in 'ST' and protein[i+3] != 'P'
        if N_glyc_check is True:
            motif_table[index].append(str(i+1))
        else: 
            continue

# remove proteins with no n-glyc motifs
motif_table = list([x for x in motif_table if len(x)> 1])

print('\n~~~~~~~~~~~~\n')

put(f"{fasta_table}",'mrpt_data')

for i in motif_table:
    print(i[0])
    print(' '.join(i[1:]))


        
