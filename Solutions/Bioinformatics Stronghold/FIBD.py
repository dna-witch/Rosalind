### Solutions to Rosalind Bioinformatics Stronghold ###
### Mortal Fibonacci Rabbits ###
file_name = "rosalind_fibd.txt"
file = open(file_name, "rt").read().split()
file = list(map(int, file))

n = file[0]
k = file[1]
