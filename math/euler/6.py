from functools import reduce

x1 = range(1,101)
x2 = range(1,101)

sum1 = (reduce(lambda x,y: x + y, x1))**2
sum2 = reduce(lambda x,y: x + y**2, x2)

print(sum1)
print(sum2)

print(sum1-sum2)