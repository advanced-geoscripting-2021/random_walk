#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Random Walk Simulation """

# Python code for 2D random walk.
# Source: https://www.geeksforgeeks.org/random-walk-implementation-python/
import numpy
import matplotlib.pyplot as plt
import random

def usr_input():
    # command line stuff
    pass


# filling the coordinates with random variables
def normal_walker(n, x, y):
    for pos in range(1, n):
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

def fast_walker():
    pass

def add_landscape():
    pass

def some_other_wlaker():
    pass


# plotting the walk
def plot_walk(n, x, y):
    plt.title("Random Walk ($n = " + str(n) + "$ steps)")
    plt.plot(x, y)
    plt.savefig("./rand_walk_{}.png".format(n))
    plt.show()


def main():
    #TODO document in the README

    # defining the number of steps
    n = 10000

    # creating two array for containing x and y coordinate
    # of size equals to the number of size and filled up with 0's
    x = numpy.zeros(n)
    y = numpy.zeros(n)

    # multiple walkers
    normal_walker(n, x, y)

    plot_walk(n, x, y)


if __name__ == "__main__":
    main()