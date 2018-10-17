library(stringr)
library(readr)

s <- read_file("c:/Users/Owner/Desktop/Rosalind/rosalind_dna.txt")

a <- "A"
g <- "G"
c <- "C"
t <- "T"

countA <- str_count(s, a)

countG <- str_count(s, g)

countC <- str_count(s, c)

countT <- str_count(s, t)

ans <- c(countA, countC, countG, countT)
ans