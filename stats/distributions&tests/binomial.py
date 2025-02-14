# creating a simple binomial calculator
# binomial graph creator
# add cumulative capabilities

#import reduce function
from functools import reduce

#factorial calculator using llmabda Functions and reduce
def fact(x):
    return reduce(lambda a, b: a*b, range(1,x+1))

n = int(input("How many trials? "))
k = int(input("Number of successes? "))
p = float(input("Probability of success on a single trial (0.0 - 1.0)? "))

#P(k yes outcomes) = P^K * (1-P)*(n-k) * # of k yes sequences


#probability a sequence with k successes
p_k = p ** k * (1 - p) ** (n - k)

# # of k yes sequences
c = fact(n) / (fact(k) * fact(n-k))

# print values
print(p_k)
print(c)
print(p_k * c)
