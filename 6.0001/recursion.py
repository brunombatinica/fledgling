# Recursive functions...


def rec_mult(a,b):
    temp = a
    if b > 1:
        temp = temp + rec_mult(a,b-1)
    elif b == 1:
        return a
    
    return temp


#Cleaner version
def rmult(a,b):
    if b == 1:
        return a
    return a + rmult(a,b-1)


print(rec_mult(5,4))
print(rmult(5,4))



def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(6))


#Towers of Hanoi in games

