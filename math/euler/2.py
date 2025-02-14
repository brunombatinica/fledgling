#https://projecteuler.net/problem=2
# fibonacci sequence and return how sum of even values

# slow but safe method



a = [1,1]
b = [0,0]

count = 0

while a[1] < 4000000:
    if a[1]%2==0:
        count += int(a[1])
        print("counting",a[1],)
        print("count",count,)
    print(a)
    b[1] = sum(a)
    b[0] = int(a[1])
    a = b[:] #stupid object oriented language



print(a)




'''
#?other possibilities to make ahuge list of hte fibonacci sequnce
a = [1,1]

while a[-1] < 10:
    a.append(a[-1]+a[-2])

print(a)

sum()
'''
