# %%


# simple program to display vectors adn vector addition

#importing important functions
import numpy as np
import matplotlib as npl
import matplotlib.pyplot as plt

x = 5.0 #input("x component: ")

y = 2.0 #input("y component: ")

V = np.array([[6,2],[-2,2]])

#Vector addition
#np.append(V, V[:,0] + V[:,1], axis = 0)
V = np.append(V, [V[0,:] + V[1,:]], axis = 0)

origin = np.zeros((len(V[:,0]),2)) # origin point, in different dimensios that V due to the way it is called *origin returns each column

#visualising the addition by stacking vector 2 on vector 1
V = np.append(V, [V[1,:]], axis = 0)
origin = np.append(origin, [V[0,:]], axis = 0)

#debugging print functions
print(origin)
print(V)

fig, ax = plt.subplots()

#######################################
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
########################################

#acutal plot function
#ax.quiver(*origin,V[:,0],V[:,1],color = "r", angles='xy', scale_units='xy', scale=1)
ax.quiver(origin[:,0],origin[:,1],V[:,0],V[:,1],color = ("r", "r", "b", "g"), angles='xy', scale_units='xy', scale=1)

#saves pdf and displays plot
#fig.savefig("vector.pdf")
plt.show()
