import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x_ = np.arange(-5,5,0.5)
y_ = np.arange(-5,5,0.5)
X,Y = np.meshgrid(x_,y_)

V = np.array([0,0])
c = [] 

#original equation  
vx1 = X*Y
vy1 = Y**2 - X**2

#derivative with respect to x
vx2 = Y
vy2 = -2*X

V = np.zeros((len(vx1.flatten()),2))
c= [] 
for i, (x,y) in enumerate(zip(vx1.flatten(),vy1.flatten())):
    V_ = np.array([[x,y]])
    c.append(np.linalg.norm(V_))
    V_ = V_ / (np.linalg.norm(V_)+1e-5)
    V[i,:] = V_
    
dV_dx = np.zeros((len(vx2.flatten()),2))
c= [] 
for i, (x,y) in enumerate(zip(vx2.flatten(),vy2.flatten())):
    V_ = np.array([[x,y]])
    c.append(np.linalg.norm(V_))
    V_ = V_ / (np.linalg.norm(V_)+1e-5)
    dV_dx[i,:] = V_
    
    
#normalize c
c = c/max(c)

print(V)
fig = plt.figure
ax1 = plt.subplot(1,2,1)
ax1.quiver(X,Y,V[:,0],V[:,1], c)

ax2 = plt.subplot(1,2,2)
ax2.quiver(X,Y,dV_dx[:,0],dV_dx[:,1])


#MAKES SENSE!!!!