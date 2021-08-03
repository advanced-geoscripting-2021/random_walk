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
def walker(n, step_size, x, y):
    """
    Normal random walker with step size 1
    :param n: number of steps
    :param x: empty numpy array consisting of n zeros
    :param y: empty numpy array consisting of n zeros
    :return: x, y numpy arrays
    """
    for pos in range(1, n):
        direction = random.randint(1, 4)
        # go east
        if direction == 1:
            x[pos] = x[pos - 1] + step_size
            y[pos] = y[pos - 1]
        # go west
        elif direction == 2:
            x[pos] = x[pos - 1] - step_size
            y[pos] = y[pos - 1]
        # go north
        elif direction == 3:
            x[pos] = x[pos - 1]
            y[pos] = y[pos - 1] + step_size
        # go south
        else:
            x[pos] = x[pos - 1]
            y[pos] = y[pos - 1] - step_size
    return x, y


def add_landscape():
    pass

def some_other_wlaker():
    # maybe morsche neighbourhood
    pass


# plotting the walk
def plot_walk(n, x, y):
    plt.title("Random Walk ($n = " + str(n) + "$ steps)")
    plt.plot(x, y)
    plt.savefig("./rand_walk_{}.png".format(n))
    plt.show()


def main():
    #TODO document everything in the README

    # defining the number of steps
    n = 10000

    # creating two array for containing x and y coordinate
    # of size equals to the number of size and filled up with 0's
    x = numpy.zeros(n)
    y = numpy.zeros(n)
    step_size = 10
    # multiple walkers

    normal_walker(n, step_size, x, y)

    # x, y = fast_walker(n, x, y)
    plot_walk(n, x, y)


if __name__ == "__main__":
    main()