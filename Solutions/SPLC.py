import sys
sys.path.append(sys.path[0] + '/..')
from rsx.tools import *
from rsx.proteins import translate

raw = get('Datasets/sample.txt')
data = fasta_strings(raw)
s_id = (list(data.keys()))[0]
s = data[s_id]
# print(s)

introns = tuple(data.values())[1:]
for i in introns:
    s = s.replace(i, '')

sc = reverse_complement(s)[::-1]
# print(s)

mRNA = transcribe(sc)
protein = translate(mRNA)

print(protein)