import sys
sys.path.append(sys.path[0] + '/..')

from rsx.tools import get

s = get('Datasets/rosalind_rna.txt')
st = ''

for i in s:
    if i == 'T':
        st += 'U'
        continue
    st += i

print(st)