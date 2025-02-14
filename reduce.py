#playing with the reduce() function & lambda functions
#takes first 2 terms feeds into function and result replaces the 2nd term

from functools import reduce

a = range(1,10)

# using traditional function
def sum(a,b):
    print(a,b)
    return a*b

c = reduce(sum,a)
print c

d = range(1,2)

#using lambda
e = reduce(lambda a, b: a*b, [1,2])
print e

reduce(lambda a, b: print(a,b), [1,2])
