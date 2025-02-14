#manually compute eulers number
# 4 ways to multiply a list  https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/
# can compare how long it takes each of them using the time function

import math

#multiply list function
from functools import reduce


#input degree of accurate
k = int(input("To what k do you want to compute e?... "))

e = 1

for i in range(2,k):
        e += 1.0/reduce(lambda a, b: a * b , range(1,i))


print("e = {}".format(e))
