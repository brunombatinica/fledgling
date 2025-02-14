#efficient fibonacci using dictionaries adn recursion



#Fibonacci numbers

def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n-1)+fib(n-2)

# My way - doeesnt work done need to feed dictionary back it is defined 
#In the first varaible scope 
def dicfib1(n,d):
    if n == 1 or n == 0: #or just supply d = {1:1,2:1}
        d = {n:1}
        return (1,d)
    else:
        if n in d:
            return d[n],d
        else:
            output = dicfib1(n-1,d) + dicfib1(n-2,d)
            d[n] = output
            return output
 
    
#Eric grimson's way
def dicfib2(n,d):
    if n in d:
        return d[n]
    else:
        output = dicfib2(n-1,d) + dicfib2(n-2,d)
        d[n] = output
        return output
    
    
#?do it with lists????
def lsfib(n,l):
    if n in range(len(l)):
        return d[n]
    else:
        output = lsfib(n-1,l) + lsfib(n-2,l)
        l.append(output)
        return output
    

d = {1:1,2:1}
l = [0,1,1]
print(dicfib2(100,d))
print(lsfib(100,l))