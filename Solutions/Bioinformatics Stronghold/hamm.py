### Rosalind Problems ###
### Counting Point Mutations ###

file_name = "rosalind_hamm.txt"
file = open(file_name, "rt").readlines()

s = file[0]
t = file[1]
hamm = 0
for i, j  in zip(s, t):
    if i != j:
        hamm += 1

print(hamm)
