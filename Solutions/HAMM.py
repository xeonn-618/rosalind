
import sys
sys.path.append(sys.path[0] + '/..')
from rsx.tools import *

raw_data = get('Datasets/rosalind_hamm.txt').split('\n')

string_1 = raw_data[0]
string_2 = raw_data[1]

print(hammingdist(string_1,string_2))
