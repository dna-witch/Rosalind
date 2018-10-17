### Rosalind Bioinformatics Armory ###

from Bio.Seq import Seq

file_name = "rosalind_arm_ini.txt"
s = open(file_name, "rt").read()
my_seq = Seq(s)

print(my_seq.count("A"), my_seq.count("C"), my_seq.count("G"), my_seq.count("T"))
