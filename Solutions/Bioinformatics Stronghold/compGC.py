### Solutions to Rosalind Bioinformatics Stronghold ###
### Computing GC Content ###
### https://github.com/fernandoBRS/Rosalind-Problems/blob/master/gc.py ###

# need to read each FASTA individually! delimiters are the line after the '>' to the '>'
file_name = "rosalind_gc.txt"
s = open(file_name, "rt").readlines()

# need to read the FASTA ID! delimiters are '>' to ' '
# make a dictionary with the FASTA IDs and GC content (see dictionary problem)
gc_content = {} # empty dictionary
dna = '' # empty string variable
# write a loop to calculate GC content
# find the highest GC content

for i in s:
    if i[0] == '>':
        dna = i[1:].rstrip() # used rstrip() because wanna get rid of the '/n' at the end
        gc_content[dna] = ''
    else:
        gc_content[dna] += i.rstrip()

# at this point, we've made a dictionary that contains the FASTA IDs and the corresponding DNA

# now, we iterate over the dictionary using items() to calculate the gc content from each DNA string
for id, fasta in gc_content.items():
    gc_content[id] = (float(fasta.count("G") + fasta.count("C")) / len(content)) * 100

(id_best, gc_best) = max(list(gc_content.items()), key = lambda item:item[1])

print(id_best)
print(gc_best)
