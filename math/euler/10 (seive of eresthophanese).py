#Summation of primes

#use seive of eristhophenies



def unique_factors(n):
    factors = [2]
    
    for i in range(2,n+1):
        unique = True
        for j in factors:
            if i % j == 0:
                unique = False
        if unique:
            factors.append(i)

    return factors




def seive_of_eratosthenes1(n):
    
    primes = list(range(2,n+1))
    
    for i in unique_factors(int(n**0.5)):
        print(i)
        for j in range(-2 + 2*i,len(primes),i):
            primes[j] = ""
        
    return primes


def seive_of_eratosthenes2(n):
    # input = number for which to find all primes below
    # output = list of all primes below that number
    
    #bprimes is an array of boolean values index by integers 2 to n
    bprimes = [True for i in range(2,n+1)]
    
    for i in range(2,int(n**0.5)):
        # indexed at - 2
        if bprimes[i-2]:
            #i ** 2 will be the smallest possible unique factor
            for j in range(i**2,n,i):
                bprimes[j-2] = False
    
    # Convert boolean list into list of primes
    primes = []
    for i in range(0,n-2):
        if bprimes[i]:
            primes.append(i+2)

    return primes

#Next steps...segmented seive, eulers seive

n = 2000000
print(seive_of_eratosthenes1(n))   
        
# even better way - start with 2 and then move on to next prime number...

print(sum(seive_of_eratosthenes2(n)))


