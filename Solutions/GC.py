import sys
sys.path.append(sys.path[0] + '/..')

from rsx.tools import *

data = get('Datasets/rosalind_gc.txt')
dataset = fasta_strings(data)

def GC_ratio(s:str) -> float:
    '''Returns the ratio of (G+C)/(A+T) content in 
    a string s'''
    A,T,G,C = basecount(s)
    return (G+C)/(G+C+A+T) # type: ignore

label = 0
highest = 0
for i in dataset:
    dna_string = dataset[i]
    ratio = GC_ratio(dna_string)
    if  ratio > highest:
        highest = ratio
        label = i

GC_per = highest*100
print(f'{label}\n{GC_per:.6f}')