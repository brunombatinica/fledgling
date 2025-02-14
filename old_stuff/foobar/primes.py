# Written in python 2 syntax

def primelist(n):
    #Funtion: returns a list of all primes below n
    #uses seive of esatasthenes
    # Input: n = integer
    # Output: list of all primes lower than n

    #Treat indexes as the actual number
    #Set 0 and 1 to be False:
    prime_position = [False, False]
    #Set rest to be true
    prime_position.extend([True for i in range(n + 1)])

    #Use the seive (highest possible unique factor is sqrt(n)
    i = 2
    while i < n**0.5:
        for j in range(i ** 2, n + 1, i):
            prime_position[j] = False
        #find the smallest possible True
        i = prime_position.index(True,i+1)


    primes = []
    for i,x in enumerate(prime_position):
        if x == True:
            primes.append(i)

    return primes


def solution(i):
    #  Create the string (length 10005)
    string = ""
    #*tricky how to tell exactly how many primes you will need....
    # for now I worked it out brute force but could work out a general solution (I am jsut lazy)
    #use not prefectly optimized (cna be done in the future if required)
    for j in primelist(20250):
        string += str(j)

    id_num = ""
    for k in range(i,i + 5):
        id_num += string[k]

    return id_num
