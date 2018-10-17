### Solutions to Rosalind Bioinformatics Stronghold ###
### Translating RNA into Protein ###

file_name = "rosalind_prot.txt"
rna = open(file_name, "rt").read()

# create a dictionary with all the codons and their respective amino acid keys
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

def protein_seq(rna):
    seq = ''

    for i in range(0, len(rna), 3):
        aa = codon_table[rna[i:i+3]]
        if aa == 'STOP_CODON':
            break
        seq += aa

    print(seq)

protein_seq(rna)
