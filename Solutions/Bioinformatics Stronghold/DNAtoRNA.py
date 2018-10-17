### Transcribing DNA into RNA ###

file_name = "rosalind_rna.txt"
s = open(file_name, "rt").read()

v = s.replace("T", "U")

print(v)
