import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Fixing random state for reproducibility
np.random.seed(19680801)


def random_walk(num_steps, max_step=0.05):
    """Return a 3D random walk as (num_steps, 3) array."""
    start_pos = np.random.random(3)
    steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
    walk = start_pos + np.cumsum(steps, axis=0)
    return walk


def update_lines(num, lines):
    
    #point 1 = position
    x1 = [0,0.5]
    y1 = [0,0.5]
    z1 = [0,0.5]
    
   
    xlist = [x1]
    ylist = [y1]
    zlist = [z1]
    
    #line 4 = acceleration
    
    for lnum, line in enumerate(lines):
        line.set_data_3d(xlist[lnum],ylist[lnum],zlist[lnum]) #set data for each line seperately
        
    return lines





# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")


lines = []
line_colors = ["red","blue","orange","green","gray"]
line_format = ["o-","-","-","-","-"]
for i in range(1):
    line_object, = ax.plot([],[],[]) #ro places points at hte end of the line
    lines.append(line_object)
    

# Setting the axes properties
ax.set(xlim3d=(0, 1), xlabel='X')
ax.set(ylim3d=(0, 1), ylabel='Y')
ax.set(zlim3d=(0, 1), zlabel='Z')

# Creating the Animation object
ani = animation.FuncAnimation(
    fig, update_lines, frames = 100, fargs= (lines,), interval=100)

plt.show()