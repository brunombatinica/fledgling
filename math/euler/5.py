# -*- coding: utf-8 -*-

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

answer = False
n = 2520 #starting point


while not answer:
    temp = True
    for i in range(1,20):
        if n % i != 0:
            temp = False
            break
    
    if temp:
        answer = n
    
    #increment by at least this amount
    n += 2520
    
print(answer)

# =============================================================================
# SOME CLEVER COOKIES SOLUTION...
#
# This does not require programming at all. Compute the prime factorization of each number from 1 to 20, and multiply the greatest power of each prime together:
# 
# 20 = 2^2 * 5
# 19 = 19
# 18 = 2 * 3^2
# 17 = 17
# 16 = 2^4
# 15 = 3 * 5
# 14 = 2 * 7
# 13 = 13
# 11 = 11
# 
# All others are included in the previous numbers.
# 
# ANSWER: 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232 792 560
#     
# =============================================================================
