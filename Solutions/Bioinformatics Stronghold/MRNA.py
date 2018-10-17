### Rosalind Problems ###
### Inferring mRNA from Protein ###

# open and read our file
file_name = "rosalind_mrna.txt"
protein_seq = open(file_name, "rt").read().strip() #strip or split?

codon_table = {

    'UUU': 'F',         'CUU': 'L',     'AUU': 'I',     'GUU': 'V',

    'UUC': 'F',         'CUC': 'L',     'AUC': 'I',     'GUC': 'V',

    'UUA': 'L',         'CUA': 'L',     'AUA': 'I',     'GUA': 'V',

    'UUG': 'L',         'CUG': 'L',     'AUG': 'M',     'GUG': 'V',

    'UCU': 'S',         'CCU': 'P',     'ACU': 'T',     'GCU': 'A',

    'UCC': 'S',         'CCC': 'P',     'ACC': 'T',     'GCC': 'A',

    'UCA': 'S',         'CCA': 'P',     'ACA': 'T',     'GCA': 'A',

    'UCG': 'S',         'CCG': 'P',     'ACG': 'T',     'GCG': 'A',

    'UAU': 'Y',         'CAU': 'H',     'AAU': 'N',     'GAU': 'D',

    'UAC': 'Y',         'CAC': 'H',     'AAC': 'N',     'GAC': 'D',

    'UAA': 'STOP_CODON',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',

    'UAG': 'STOP_CODON',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',

    'UGU': 'C',         'CGU': 'R',     'AGU': 'S',     'GGU': 'G',

    'UGC': 'C',         'CGC': 'R',     'AGC': 'S',     'GGC': 'G',

    'UGA': 'STOP_CODON',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',

    'UGG': 'W',         'CGG': 'R',     'AGG': 'R',     'GGG': 'G'

}

def codon_freq():
    freq = {}
    for k, v in codon_table.items():
        if v not in freq:
            freq[v] = 1
            freq[v] += 1
    return freq

def poss_rna_strings(protein_seq):
    f = codon_freq()
    n = f['STOP_CODON']
    for i in protein_seq:
        n *= f[i]
    return n

print(poss_rna_strings(protein_seq) % 1000000)
