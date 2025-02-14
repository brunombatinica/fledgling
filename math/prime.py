# prints all the prime numbers up to the value specified by the user
# ?try seive method...
# https://stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python




#inputs - blank for now
inputmax = input("print primes below ... (integer > 2) ")

#timer (after inputs)
import time
start_time = time.time()

import math

# bad code as 2 breaks the test but is a prime (actually you need to do this hahahahahha)
#print 2
count = 1
prime = True

# test only odd numbers from 3
for i in range(3,inputmax,2):
    #test numbers against (2 to sqaure root i)
    for j in range(3,int(math.sqrt(i)+1),2):
        if i%j == 0:
            prime = False
            break
        else:
            pass
    if prime:
        #print hidden
        #print i
        count += 1
    prime = True

# display count
print("primes below input = "+str(count))

#display time
print time.time() - start_time, 's'
