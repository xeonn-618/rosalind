import sys
sys.path.append(sys.path[0] + '/..')

import rsx.tools

s = rsx.tools.get("Datasets/rosalind_revc.txt")

result = rsx.tools.reverse_complement(s)

rsx.tools.put(result,'rosalind_revc')

