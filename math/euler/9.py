# Pythagorean triplet


def pytrip(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def bisearch(lower,upper):    
    test = upper ** 2 - lower ** 2
    counter = 0
    
    while counter < 10:
        b = round((upper + lower)/2)
        if b**2 == test:
            return b
        if b**2 > test:
            upper = b
        elif b**2 < test:
            lower = b
        counter += 1
        
    return False
        
solved = 0

c = 1000

while not solved and c > 0:
    c -= 1
    a = 1
    while 1 <= a <= c:
        a += 1
        b = bisearch(a,c)
        if b:
            if (a + b + c) == 1000:
                print(a,b,c)
                print("SOLVED!!")
                solved = 1
            pass
        
    