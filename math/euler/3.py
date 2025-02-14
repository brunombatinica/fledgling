# Largest prime factor

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

import math

"""
#def a generator for looping over odd numbers
def odds(stream):
    for n in stream:
        if not n % 2 == 0:
            yield n

a = range(100)
print(list(odds(a)))
"""

# function that checks if prime
def is_prime(num):
    # test negatives
    if num < 2:
        return False

    # test 2
    if num == 2:
        return True

    #test even
    if num % 2 == 0:
        return False

    # test rest
    for i in range(3,int(math.sqrt(num))+1,2):
        if num % i == 0:
            return False

    return True

print(is_prime(29))

#initialize list of prime factors
pf = []

# set number
n = int(input("what number do you want to find the highest prime factor for? ... "))

#test 2
if n % 2 == 0:
    pf.append(2)

print(n)

#test all other possible factors (odd numbers up untill n%2)
for i in range(3, int(n / 2) ,2):
    if n % i == 0 and is_prime(i):
        print(i)
        pf.append(i)

print(pf)
