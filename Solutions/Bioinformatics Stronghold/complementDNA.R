library(stringi)
library(stringr)
library(readr)

# remember to replace the sample string with the read_file("~/file_name.txt")
s <- read_file("c:/Users/Owner/Desktop/Rosalind/rosalind_revc.txt")
s <- stri_reverse(s)

# look more into chartr

sC <- chartr("AGCT", "TCGA", s)
sC