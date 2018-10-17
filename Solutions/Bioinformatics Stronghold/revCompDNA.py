### Complementing a Strand of DNA ###

file_name = "rosalind_revc.txt"
s = open(file_name, "rt").read()

v = s[::-1] # use a string slice that steps by -1 to reverse the string

# can use a for loop, or you can do this (got the idea from Veronica)
# the .upper() idea was taken from the posted Rosalind solutions
vComp = v.replace("A", "t").replace("C", "g").replace("G", "c").replace("T", "a").upper()

print(vComp)
