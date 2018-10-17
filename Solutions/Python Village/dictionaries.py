### Solutions to Rosalind Problems
### "Dictionaries"

file_name = "rosalind_ini6.txt"
s = open(file_name, "rt").read().split(" ")
v = list(map(str, s))
dict = {}

for word in v:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

for word in dict:
    print(word + " " + str(dict[word]))
