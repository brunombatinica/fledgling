import numpy as np
from turtle import *
#imports everything...


def branch(n):
    #n = size of branch 
    #s = size
    
    if n == 0:
        dot(0)
        
    else:
        # #t = angle
        # t = np.pi/6
        # rule of thumb let s = 200/n
        s = 20 * n
        #set width
        width(n)
        
        #Draw left branch
        left(t)
        forward(s)
        
        #recursive
        branch(n-1)
        
        #reset width
        width(n)
        
        #draw right branch
        right(np.pi)
        forward(s)
        left(np.pi - 2*t)
        forward(s) 
        
        #recursive
        branch(n-1)
        
        #return to start
        right(np.pi)
        forward(s)
        right(np.pi - t)
        



#Set intiial position and direction and hide turtle
mode("logo")
radians()
speed(0)
hideturtle()
penup()
setheading(0)
sety(-300)
pendown()

num = 6
t = np.pi/10

width(num)
#Draw turnk
forward(150)

#Draw branches
branch(num-1)

done()