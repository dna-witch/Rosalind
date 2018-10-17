### Solutions to Rosalind Problems
## "Strings and Lists"

file_name = "rosalind_ini3.txt" # <insert name of Rosalind dataset here>
s = open(file_name, "rt").readlines()

string = s[0]
index = s[1]
v = index.split()
v = list(map(int, v))

for i = 0 in v:
    a = v[i]
    b = v[i+1]
    c = v[i+2]
    d = v[i+3]
print(string[a:b+1] + " " + string[c:d+1])
