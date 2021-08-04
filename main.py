#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Random Walk Simulation """

# Python code for 2D random walk.
# Source: https://www.geeksforgeeks.org/random-walk-implementation-python/

import matplotlib.pyplot as plt
from randomwalk import Walker

import numpy
import matplotlib.pyplot as plt
import random
from randomwalk import Walker

# defining the number of steps
n = 100000

walker1 = Walker(100, 100)
walker2 = Walker(200, 200)
for i in range(1, n):
    walker1.walk()
    walker2.walk()

# plotting the walk
plt.title("Random Walk ($n = " + str(n) + "$ steps)")
plt.plot(walker1.x_coords, walker1.y_coords)
plt.plot(walker2.x_coords, walker2.y_coords)
plt.savefig("./rand_walk_{}.png".format(n))
plt.show()
