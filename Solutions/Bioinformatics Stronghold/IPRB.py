### Rosalind Problems ###
### Mendel's First Law ###
from scipy.special import comb

file_name = "rosalind_iprb.txt"
s = open(file_name, "rt").read().split()

# k = homozygous dominant (dominant phenotype)
# m = heterozygous (dominant phenotype)
# n = homozygous recessive (recessive phenotype)
k = int(s[0])
m = int(s[1])
n = int(s[2])

def mendel(k, m, n):
    totalPop = k + m + n
    twoRec = (n/totalPop)*((n-1)/(totalPop - 1))
    twoHet = (m/totalPop)*((m-1)/(totalPop - 1))
    hetRec = (n/totalPop)*(m/(totalPop - 1)) + (m/totalPop)*(n/(totalPop - 1))
    probRec = twoRec + twoHet*0.25 + hetRec*0.5
    probDom = 1 - probRec #take the complement!
    print(probDom)

print(mendel(k, m, n))
