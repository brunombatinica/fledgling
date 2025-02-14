def fib(n):
    #beautiful but slow
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
    
def fastfib(n, memo = {}):
    #store previous computations
    
    if n == 0 or n == 1:
        return 1
    
    try:
        return memo[n]
    except:
        l = fastfib(n-1,memo)
        r = fastfib(n-1,memo) 
        memo[n] = l
        
        return l+r
    
print(fib(20))
print(fastfib(120))