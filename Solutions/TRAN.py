import sys
sys.path.append(sys.path[0] + '/..')

from rsx.tools import *

raw = get('Datasets/sample.txt')
data = list(fasta_strings(raw).values())
s1, s2 = data[0], data[1]

# print(s1)
# print(s2)

# print(hammingdist(s1,s2))
trn = transitionCount(s1,s2)
tnv = transversionCount(s1,s2)
# print(trn, tnv)

ratio = trn/tnv
print(ratio)