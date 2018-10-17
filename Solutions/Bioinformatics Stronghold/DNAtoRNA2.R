library(stringr)
library(readr)

t <- read_file("c:/Users/Owner/Desktop/myProjects/Rosalind/rosalind_rna.txt")

u <- str_replace_all(t, "T", "U")

u
