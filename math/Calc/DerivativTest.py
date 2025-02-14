import numpy as np
from scipy.misc import derivative
from functools import reduce

#importing important functions
import matplotlib as npl
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

x_limit = [-10,10]
# The maths.....


# The maths.....
def fun(x):
    # What function we want to examine
    return np.cos(x)

def odd_increment(n):
    #returns the smallest odd number that is > n
    if n%2 == 0:
        return n + 1
    else:
        return n + 2
    
def fact(n):
    # returns n factorial
    if n == 0:
        return 1
    else:
        return reduce(lambda x,y: x*y,range(1,n+1))

def taylor_coef(fun,i):
    #input integer i and equation func
    #returns a float of the ith coeficient of hte taylor equation
    
    #work out coefficients
    #Computed at 0
    return float(derivative(fun, 0, n = i, dx= 0.0001, order = odd_increment(i))/fact(i))

print(derivative(fun, 0, n = 11, dx= 0.1, order = 15))
print(taylor_coef(fun,5))

def taylor_func(coefficients,x):
    #Taylor function takes an input flot x and list coefficients:
    #Returns the value of y
    y = 0.0
    for degree,coef in enumerate(coefficients):
        y += coef * (x ** degree)
        
    return y    
  


#plot figure
fig, ax = plt.subplots()


lines = []
for i in range(2):
    line_object, = ax.plot([],[])
    lines.append(line_object)

x = np.arange(*x_limit,0.1)

y1 = taylor_func([1,0,2],x)

coef = []
coef.append(taylor_coef(fun,0))

print(coef)
y2 = fun(x)

xlist = [x,x]
ylist = [y1,y2]


for lnum, line in enumerate(lines):
    line.set_data(xlist[lnum],ylist[lnum])


#puts grid on the plot
ax.grid()
#sets axes (default on)
ax.set_axis_on()
#set specific axis limits
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
#moving axis to middle of plot (using spines)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

#acutal plot function
ax.plot(x,y1,color = "C1")

#saves pdf and displays plot
#fig.savefig("gaussian_distribution.pdf")
plt.show()
