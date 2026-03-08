file = open('Datasets/rosalind_dna.txt', 'r')
data = file.read()
file.close()

result = ''

for base in "ACGT":
    result += str(data.count(base)) + ' '

with open("Outputs/rosalind_dna_output.txt", "w") as f:
    f.write(result)
    f.close()
