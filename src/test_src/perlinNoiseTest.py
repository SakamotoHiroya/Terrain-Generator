import sys
sys.path.append('../')

import perlinnoise as pn
import matplotlib.pyplot as plt
import numpy as np
import random

# set seed value in 0 ~ 100000
seed = random.randint(0, 100000)

x = y = np.arange(-3, 3, 0.05)

X, Y = np.meshgrid(x, y)

z = pn.noise(X, Y, seed=seed, maxSlope=1)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(X, Y, z, cmap='terrain')
ax.view_init(elev=90, azim=0)

plt.show()