# find the 10001 prime....

import math

#?brute force
# check ever odd number

def isprime(x):
    # test for 2
    if x == 2:
        return True
    #test if even
    if x % 2 == 0: 
        return False
    
    for i in range(3,int(math.sqrt(x))+1,2):
        if x % i == 0:
            return False
        
    return True


count = 0
i = 1

while count <= 10000:
    i += 1
    if isprime(i):
        count += 1
    
print(i)