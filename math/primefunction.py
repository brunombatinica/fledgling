# do a time check for geneartor function - waste of time ahahhahah

import time
import math

start1 = time.time()

#odds function
def odds(stream):
    for n in stream:
        if not n % 2 == 0:
            yield n

# function that checks if prime
def is_prime1(num):

    # test rest
    for i in odds(range(3,int(math.sqrt(num))+1)):
        if num % i == 0:
            return False

    return True

b = [is_prime1(x) for x in range(1,1000000)]

stop1 = time.time()

start2 = time.time()

def is_prime2(num):
    for i in range(3,int(math.sqrt(num))+1,2):
        if num % i == 0:
            return False

    return True

c = [is_prime2(x) for x in range(1,1000000)]


stop2 = time.time()

print("time 1 =", start1 - stop1)
print("time 2 =", start2 - stop2)
