### Counting DNA Nucleotides ###

# solution 1
# this is for some reason multiplying the counts by 3

file_name = "rosalind_dna.txt"
s = open(file_name, "rt").read()
counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0} # make a dictionary
v = s.replace("\n", "") # this is to fix the KeyError: '\n' that pops up

for i in v:
    counts[i] += 1

ans = (counts['A'], counts['B'], counts['C'], counts['D'])
print(ans)


# solution 2
file_name = "rosalind_dna.txt"
s = open(file_name, "rt").read()
def freq(s):
    return s.count("A"), s.count("G"), s.count("C"), s.count("T")

freq(s)
