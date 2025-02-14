import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import random

class line(object):
    def __init__(self,b0,b1,b2):
        self.b0 = b0
        self.b1 = b1
        self.b2 = b2  
    
    def plot(self,ax):
        x1 = np.arange(0,10,0.1)
        #bad form directly indexing but i am lazy
        b0 = self.b0
        b1 = self.b1
        b2 = self.b2
        x2 = (b1*x1 + b0)/ (-1 * b2)
        ax.plot(x1,x2,alpha = 0.5, color = "grey")
        
    def ortho(self,x0):
        #returns an orthogonal vector at x0
        b0 = self.b0
        b1 = self.b1
        b2 = self.b2
        
        # #convert paramteric to vector form
        # x1 = b2
        # y1 = -1*b1
        
        # x2 = -1
        # y2 = -1* (x1*x2 / y1) 
        
        # #find where x0 equates to on the line
        # y0 = (b1*x0 + b0)/ (-1 * b2)
        # return vector(x2,y2,x0,y0).unit()
    
        #Shortcut
        y0 = (b1*x0 + b0)/ (-1 * b2)
        return vector(b1,b2,x0,y0).unit()
    
    def margin(self,x,y):
        #returns hte distance from the line to
        # the point x,y
        
        b0 = self.b0
        b1 = self.b1
        b2 = self.b2
        
        return (b1*x +b2*y +b0)/(b1**2 + b2**2)**0.5
    
class vector(object):
    def __init__(self,x,y,x0,y0):
        self.x = x
        self.y = y
        self.x0 = x0
        self.y0 = y0
    
    def ori(self,x0,y0):
        self.x0 = x0
        self.y0 = y0
        
    def norm(self):
        return (self.x**2 + self.y**2)**0.5
    
    def unit(self):
        x = self.x
        y = self.y 
        n = self.norm()
        #this is why it is stupid to index directly
        self.x = x/n
        self.y = y/n
        
        return self
        
    def plot(self,ax):
        x0 = self.x0
        x = self.x
        y0 = self.y0
        y = self.y
        ax.plot([x0,x0+x],[y0,y0+y],
                c = "orange")
   
    def __str__(self):
        return "[{:.2f}, {:.2f}] origin [{:.2f}, {:.2f}]".format(
            self.x,self.y,self.x0,self.y0)
        
    def line(self):
        #convert vector into a line
        x0 = self.x0
        y0 = self.y0
        x = self.x
        y = self.y 
        
        b1 = self.x
        b2 = self.y
        b0 = -1*(x*x0 + y*y0)
        
        return line(b0,b1,b2)
    
    
    
##########################################
fig, ax = plt.subplots()

# set z set_axis_on
# Customize theaxis.
ax.set_xlabel("x")
ax.set_xlim(0, 10)

ax.set_ylabel("y")
ax.set_ylim(0, 10)
#############################################




##############################################    
# set points
vectors = np.empty(shape = [3,0])
random.seed(6)
for i in range(1,9):
    v = np.array([[random.randint(1,9)],
     [random.randint(1,9)]])
    #classify points based on simpe 
    # decision boundary (z - x = 0)
    c = [[1 if (v[1] - v[0] > 0) else -1]]
    
    vectors = np.append(
                vectors, 
                np.append(v,c,axis = 0), 
                axis = 1)
    

#creating line
db = line(1,1,-2)

#finding orthogonal vector
v1 = vector(2,1,0,0)
print(v1.norm())
v1.unit()

v2 = db.ortho(5)
print(v2)
v2.plot(ax)

test = v2.line()
test.plot(ax)

print(test.margin(8,0))

#plotting everything
col = ["red" if i>0 else "blue" for i in vectors[2,:]]
ax.scatter(vectors[0,:],vectors[1,:],c = col)

db.plot(ax)
v1.plot(ax)

plt.show()

