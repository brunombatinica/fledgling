import matplotlib.pyplot as plt

#for animations
import matplotlib.animation as animation
from matplotlib import style

# =============================================================================
# Basic graphs 
#
# x1 = [1,2,3]
# y1 = [5,7,4]
# 
# x2 = [1,2,3]
# y2 = [10,12,13]
# 
# # most basic plot
# plt.scatter(x1,y1, label = "line 1")
# 
# #add labels
# plt.xlabel('x')
# plt.ylabel('improtant bar')
# plt.title('interesting graph\nChek it out')
# 
# #add another line
# plt.plot(x2,y2, label = "line 2")
# 
# #add legend - need to know what to put in so need to add 
# #lable to plot function
# plt.legend()
# 
# plt.show()
# =============================================================================

# histograms






# =============================================================================
# # scatter plots
# x = range(1,8)
# y = [1,5,2,4,6,8,4]
# 
# plt.scatter(x,y, 
#             label = "skit scat", 
#             color = "k",
#             marker ="*",
#             s = 100)
# 
# #add labels
# plt.xlabel('x')
# plt.ylabel('improtant bar')
# plt.title('interesting graph\nChek it out')
# plt.legend()
# 
# 
# plt.show() #not neccesary?
# =============================================================================

#stack plot
# https://www.youtube.com/watch?v=Z81JW1NTsO8

# =============================================================================
# # subplots
# x = range(10)
# y = [1,7,5,6,8,9,3,4,5,6]
# 
# #style extra
# style.use('fivethirtyeight')
# 
# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
# 
# ax1.plot(x,y)
# 
# plt.show
# =============================================================================



# animation basics
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
x = range(1,10)
y = range(1,10)

# i is the interval
def animate(i):
    graph_data = []
    
    ax1.clear() #computationaly light
    ax1.plot(x,y)

ani = animation.Funcantimation(fig, animate, interval = 1000)    
plt.show()




