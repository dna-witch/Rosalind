### Solutions to Rosalind Problems
## "Working with Files"

file_name = "rosalind_ini5.txt" # open your file here as a string

s = open(file_name, "rt").readlines()

i = 1 # because assume 1-based numbering; remember i is a manual index
for line in s:
        if i%2 == 0:
                v = s.write(list(s[i:i+=1]))

print(v)
v.close()


# Alternative solution (some kinks)
file_name = "rosalind_ini5.txt" # open your file here as a string
f = open(file_name, 'r').readlines()
result = open('output_ini5.txt', 'w')

with open(file_name, 'r') as f:
    r = list(f)[1::2]

r = str(r)
print(r)

# Alternative solution 2 (this is my favorite)
file_name = "rosalind_ini5.txt" # file name as a string
f = open(file_name, 'r').readlines() # open input file as read-only; line by line
result = open('output_ini5_test.txt', 'w') # open/create an output file

for i in f[1::2]: # index opened input file; want to read by multiples of two
        result.write(i) # write to the output file
result.close() # close the output file
