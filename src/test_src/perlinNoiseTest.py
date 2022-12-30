import sys
sys.path.append('../')

import perlinnoise as pn
import matplotlib.pyplot as plt
import numpy as np
import random

# set seed value in 0 ~ 100000
seed = random.randint(0, 100000)

def smoothSlope(location, seed, maxSlope):
    return np.array([pn.noise(*location, seed=hash((seed, 1)), scale=1.01, maxSlope=maxSlope*2),
                     pn.noise(*location, seed=hash((seed, 2)), scale=1.01, maxSlope=maxSlope*2),
                     pn.noise(*location, seed=hash((seed, 3)), scale=1.01, maxSlope=maxSlope*2)])
    
x = y = np.arange(6, 10, 0.1)

X,Y = np.meshgrid(x, y)

z = pn.noise(X, Y, seed=seed, maxSlope=3, slopeFunc=smoothSlope) + pn.noise(X, Y, seed=hash(seed), maxSlope=2, slopeFunc=smoothSlope, scale=0.5) * 0.3 + pn.noise(X, Y, seed=hash((seed, 1)), maxSlope=1, slopeFunc=smoothSlope, scale=0.1) * 0.1

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(X, Y, z, cmap='terrain')
ax.view_init(elev=60, azim=0)

plt.show()