#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Random Walk Simulation """

# Python code for 2D random walk.
# Source: https://www.geeksforgeeks.org/random-walk-implementation-python/
import numpy as np
import matplotlib.pyplot as plt
import random
import sys


def user_input():
    try:
        walkers = int(sys.argv[1])
        steps = int(sys.argv[2])
        dif_start = bool(int(sys.argv[3]))
    except Exception as err:
        print("Incorrect input: ", err)
        sys.exit()
    return walkers, steps, dif_start


# filling the coordinates with random variables
def normal_walker(steps, x, y, dif_start):
    if dif_start is True:
        x[0] = random.randint(-10, 10)
        y[0] = random.randint(-10, 10)
    for pos in range(1, steps):
        direction = random.randint(1, 4)
        # go east
        if direction == 1:
            x[pos] = x[pos - 1] + 1
            y[pos] = y[pos - 1]
        # go west
        elif direction == 2:
            x[pos] = x[pos - 1] - 1
            y[pos] = y[pos - 1]
        # go north
        elif direction == 3:
            x[pos] = x[pos - 1]
            y[pos] = y[pos - 1] + 1
        # go south
        else:
            x[pos] = x[pos - 1]
            y[pos] = y[pos - 1] - 1
    return x, y


def multiple_walkers(steps, x, y, walkers, dif_start):
    xlist = []
    ylist = []
    for w in range(walkers):
        x_axis, y_axis = normal_walker(steps, x, y, dif_start)
        xlist.append(x_axis)
        ylist.append(y_axis)
        x = np.zeros(steps)
        y = np.zeros(steps)
    return xlist, ylist


def fast_walker():
    pass

def add_landscape():
    pass

def some_other_wlaker():
    pass


# plotting the walk
def plot_walkers(steps, walkers, xlist, ylist):
    fig = plt.figure(figsize=(8,8), dpi=200)
    ax = fig.add_subplot(111)
    color = iter(plt.cm.rainbow(np.linspace(0, 1, walkers)))
    for w in range(walkers):
        c = next(color)
        pathX = xlist[w]
        pathY = ylist[w]
        ax.scatter(pathX, pathY, color=c, alpha=0.25, s=1)
        ax.plot(pathX, pathY, color=c, alpha=0.25, lw=2, label='%s. walker' % (w+1))
        ax.plot(pathX[0],pathY[0], color=c, marker='o')
        ax.plot(pathX[-1], pathY[-1], color=c, marker='+')
    plt.legend()
    plt.title("Random Walk (Number of walkers = " + str(walkers) + ", $n = " + str(steps) + "$ steps)")
    plt.savefig(".\\rand_walk_{}_{}.png".format(walkers, steps))
    plt.show()


def main():
    #TODO document in the README

    # defining the number of steps
    walkers, steps, dif_start = user_input()
    # creating two array for containing x and y coordinate
    # of size equals to the number of size and filled up with 0's
    x = np.zeros(steps)
    y = np.zeros(steps)

    # multiple walkers
    listX, listY = multiple_walkers(steps, x, y, walkers, dif_start)

    plot_walkers(steps, walkers, listX, listY)

if __name__ == "__main__":
    main()