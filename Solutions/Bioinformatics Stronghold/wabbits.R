# A new generation each month! n = # months/generations
# k = how many new rabbit pairs per litter
wabbits <- read_file("C:/Users/Shakuntala/Desktop/myProjects/Rosalind/rosalind_fibd.txt")
n <- wabbits[1, 1]
k <- wabbits[1, 2]

# create the array and first two items
## f1 = f2 = 1
len <- n
fibvals <- numeric(len)
fibvals[1] <- 1
fibvals[2] <- 1

# calculate! fibonacci solver
for (i in 3:len) {
  fibvals[i] <- fibvals[i-1] + k*fibvals[i-2]
}

x <- fibvals[len]

print(x, digits = 16)