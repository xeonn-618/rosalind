import sys
sys.path.append(sys.path[0] + '/..')

from rsx import tools

def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)

def P(n,r):
    return (fact(n)/fact(n-r))

n = 7

permutationsCount = int(P(n,n))

# To show all permutation combinations,
# 1)  Calculate total possible combinations (All factorials of 2 and above are even)
# 2) Take the ordered sequence for n
# 3) Take out the first element from the list and append it at the back (Like a stack)
# 4) Continue until you have done n!/2 steps then
# Take the original ordered list, reverse it, and run the same algorithm

permutations = []

seq = list([x for x in range(1,n+1)])
for i in range(permutationsCount//2):
    if i == 0:
        permutations.append(seq.copy())
        continue
    seq.append(seq.pop(0))
    permutations.append(seq.copy())

seq.append(seq.pop(0))
seq = seq[::-1]

for i in range(permutationsCount//2):
    if i == 0:
        permutations.append(seq.copy())
        continue
    seq.append(seq.pop(0))
    permutations.append(seq.copy())

data = ''

print(permutationsCount)

data += str(permutationsCount) + '\n'
for perm in permutations:
    data += ' '.join(map(str, perm)) + '\n'

tools.put(data, 'PERM')