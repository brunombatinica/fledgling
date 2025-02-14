# 3D surface plot of the joint PDF of 2 standard normals with covariance
# ?Make it more pythonic in the future - the LA was too much for me



import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
# colours
from matplotlib import cm

a = np.array([1,2,3])

fig, ax = plt.subplots(subplot_kw = {"projection": "3d"})

sd = 1
mu = 0


x1 = np.arange(-4,4,0.1)
x2 = np.arange(-4,4,0.1)
#x1 = [0,1,2]
#x2 = [0,1,2] 

# X = np.arr
#x = np.array([x1,x2])
#print(x)

x1, x2 = np.meshgrid(x1,x2)
#print(mx)

#covariance matrix
cov = np.array([[1,1],[1,2]])
cov_1 = np.linalg.inv(cov)
#print("cov =")
#print(cov_1)

Y = np.zeros((len(x1),len(x2)))
X = []


# do it the non pythonic way
for i, X1 in enumerate(x1[0,:]):
    for j, X2 in enumerate(x2[:,0]):
        X = np.array([X1,X2])
        Y[i,j] = np.exp(-1*np.abs(X.T@cov_1@X))
        X = []



#z = x*y - as we are assuming the 2 gausian distributions are independent
#z = (1 / (sd * np.sqrt(2 * np.pi))) * np.exp( -0.5 * ( ((x - mu) / sd)**2 + ((y - mu) / sd)**2))
#simplified gaus
#Y = np.exp(-1*np.abs(x.T@cov_1@x))


#plot surface
surf = ax.plot_surface(x1,x2,Y, cmap=cm.coolwarm,linewidth=0, antialiased=False )

# set z set_axis_on
# Customize theaxis.
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_zlim(0, 1)

#ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
#ax.zaxis.set_major_formatter('{x:.02f}')
# Add a color bar which maps values to colors.

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
