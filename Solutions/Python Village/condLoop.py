### Solutions to Rosalind Problems
## "Conditions and Loops"

file_name = "rosalind_ini4.txt" # insert your filename here as a string
s = open(file_name, "rt").read().split()
s = list(map(int, s))

a = s[0]
b = s[1]
result = 0  # here is where we do a trick!

for i in range(a, b+1): # we want the range to be inclusive of b, so we go to b+1
        if i%2 == 1:
                result += i # x += y is the same as x = x + y, except that x is only evaluated once

print(result)
