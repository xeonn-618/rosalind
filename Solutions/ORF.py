import sys
sys.path.append(sys.path[0] + '/..')

from rsx.tools import *
from rsx.proteins import *

raw = get('Datasets/sample.txt')
dna = list(fasta_strings(raw).values())[0]

candidate_proteins = []

dnac = reverse_complement(dna)

# print(f"5'-{dna}-3'")
# print(f"5'-{dnac}-3'")

allframes = [dna,dna[1:],dna[2:],dnac,dnac[1:],dnac[2:]]

for frame in allframes:
    protein = translate(transcribe(frame))

    n_stop = protein.count('*')
    n_start = protein.count('M')

    # iterate over all *, starting with finding first * to last *
    last_stop = 0
    for s in range(n_stop):
        stop_index = protein.find('*',last_stop)
        if s>0:
            last_start = last_stop # dont start from beginning of every string
        else: last_start = 0

        # now find all starts, and find cp from first m to last m before stop index *
        for m in range(n_start):
            start_index = protein.find('M',last_start, stop_index)
            if start_index == -1: # no more M inbetween curr pos and * 
                break
            cp = protein[start_index:stop_index]
            last_start = start_index + 1 # update last start so next M is found after current M but before *
            if cp != '': candidate_proteins.append(cp)
        last_stop = stop_index + 1


# for cp in candidate_proteins:
#     print(cp)

print(len(candidate_proteins))
print(len(set(candidate_proteins)))

raw_result = '\n'.join(set(candidate_proteins))
put(raw_result,'orf_result')
