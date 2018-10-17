### Solutions to Rosalind Problems
## "Variables and Some Arithmetic"

# Simple

a = <insert number here>
b = <insert number here>
c = a**2 + b**2
print(c)

# Slightly more complex
file_name = <insert the Rosalind dataset you downloaded> # rosalind_ini2.txt
def hyp_squared(file_name): # define a function to do what you want it to do
        values = open(file_name, "rt").read().split()
        a = int(values[0])
        b = int(values[1])
        return a**2 + b**2
hyp_squared(file_name)
