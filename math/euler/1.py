#https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem
# hacker rank is bullshit
#https://codereview.stackexchange.com/questions/149143/project-euler-problems-1-and-2-in-python
# method 1 - classif fizz buzz for loop modulo testing
# method 2 - using sets sum(*{range(0,n,3)}) and bitwise perators
# method 3 - triangular numbers

'''
a = {3,6,9,12,13,15,18}
b = {5,10,15}

print(sum(range(100)))
print(b)

print(a & b)


#!/bin/python3

import sys


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    print(sum(range(3,n,3)) + sum(range(5,n,5)) - sum(range(15,n,15)))
'''
n = 1000

print(sum({*range(0,n,3)}|{*range(0,n,5)}))
# triangular numbers????
