import numpy as np
import matplotlib as mpl
from matplotlib import animation
from matplotlib import pyplot as plt
from functools import reduce
from scipy.misc import derivative

#Initialize stuff
frame_num = 13 #Number of degres
x_limit = (-10,10)
y_limit = (-10,10)


# THE FUNCTIONS....
def fun(x):
    # What function we want to examine
    #return np.cos(x)
    #return np.sin(x)   
    #return 3* np.exp(x)/(x**2 + x + 1) 
    #return np.log(x+2)
    
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
    return float(derivative(fun, 0, n = i, dx= 0.1, order = odd_increment(i))/fact(i))


def taylor_func(coefficients,x):
    #Taylor function takes an input flot x and list coefficients:
    #Returns the value of y
    y = 0.0
    for degree,coef in enumerate(coefficients):
        y += coef * (x ** degree)
        
    return y    
  
###INITIATIZE OBJECTS AND LISTS...    
  
#set up figure
fig = plt.figure()
ax1 = plt.axes(xlim = x_limit, ylim = y_limit)

#Create a list of 2 lines
lines = []
for i in range(2):
    line_object, = ax1.plot([],[])
    lines.append(line_object)

##########Calculate coefficients    
coef = []
for i in range(frame_num):
    coef.append(taylor_coef(fun,i))
print(coef)
    
    
########ANIMATION FUNCTIONS
def init():
    for line in lines:
        line.set_data([],[])
        
    return lines


def animate(i):
    x = np.arange(*x_limit,0.1)
    
    y1 = fun(x)
    y2 = taylor_func(coef[0:i+1],x)
    # y2 = taylor_func([1],x)
    
    xlist = [x,x]
    ylist = [y1,y2]
    
    
    for lnum, line in enumerate(lines):
        line.set_data(xlist[lnum],ylist[lnum])
    
    return lines



# call the animator
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=frame_num, interval=500, blit=True)

