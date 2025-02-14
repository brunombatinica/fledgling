# manual linear regression - chapter 2 ISLR2


import numpy as np

def mean(x):
    mx = sum(x)/len(x)
    return mx

#compute variance
def var(x):
    r = 0
    for i in x:
        r += ((i - mean(x)) ** 2 )/(len(x)-1)
    return r

#compute covariance
def covar(x,y):
    r = 0
    for i,j in zip(x,y):
        r += ((i - mean(x)) * (j - mean(y))) /(len(x)-1)
    return r

x = [1,2,4,5,6,9,7,6,3,5,15]
y = [1,5,3,4,5,8,9,10,4,5,16]

n = []
d = []

#compute slope "manually"
for i,j in zip(x,y):
    n.append( ((i - mean(x)) * (j - mean(y)))  )
    d.append( ((i - mean(x)) ** 2))
    b1 = mean(n)/mean(d)

#r = covar(x,y) / (np.sqrt(var(x)) * np.sqrt(var(y)))
#b1 = r * np.sqrt(var(y)) / np.sqrt(var(x))

b0 = mean(y) - b1 * mean(x)



# manual rss
resid_squared = []
for i,j in zip(x,y):
    resid_squared.append( ((j) - b1 * i - b0) ** 2 )

rss = sum(resid_squared)

print(mean(x))
print(var(x))
print(covar(x,y))
#print(r)
print(b1)
print(b0)
print(rss)
