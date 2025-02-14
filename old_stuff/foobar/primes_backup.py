

def primelist(n):
    #returns a list of all primes below n 
    #uses seive of esatasthenes

    #Treat indexes as the actual number
    # Set 0 and 1 to be false
    prime_position = [False,False,*[True for i in range(n - 1)]]
    
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
        
    return int(id_num)
    
    
print(solution(0))