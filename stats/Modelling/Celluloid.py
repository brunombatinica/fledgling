#celluloidtest

import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
from IPython.display import HTML

x = np.linspace(0, 10, 500)
y = np.sin(x)

fig = plt.figure(dpi = 300)
camera = Camera(fig)
for i in range(len(x)):
    plt.plot(x[:i], y[:i], c = 'royalblue')
    camera.snap()
    
animation = camera.animate(blit=False, interval=10)