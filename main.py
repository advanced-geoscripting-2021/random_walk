#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Random Walk Simulation """

# Python code for 2D random walk.
# Source: https://www.geeksforgeeks.org/random-walk-implementation-python/
import matplotlib.pyplot as plt
import random
import numpy as np
import math
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

def walker(x, y, steps, dif_start, step_size=1, direction_set=("NORTH", "SOUTH", "EAST", "WEST")):
    """
    Normal random walker with step size 1
    :param steps: number of steps
    :param step_size: defines the size of the steps
    :param x: empty numpy array consisting of n zeros
    :param y: empty numpy array consisting of n zeros
    :param direction_set: defines a set of directions, default values North, South, East, West
    :return: x, y numpy arrays
    """
    if dif_start is True:
        x[0] = random.randint(-10, 10)
        y[0] = random.randint(-10, 10)
    for pos in range(1, steps):
        direction = random.choice(direction_set)

        # go east
        if direction == "EAST":
            x[pos] = x[pos - 1] + step_size
            y[pos] = y[pos - 1]
        # go west
        elif direction == "WEST":
            x[pos] = x[pos - 1] - step_size
            y[pos] = y[pos - 1]
        # go north
        elif direction == "NORTH":
            x[pos] = x[pos - 1]
            y[pos] = y[pos - 1] + step_size
        # go south
        else:
            x[pos] = x[pos - 1]
            y[pos] = y[pos - 1] - step_size
    return x, y


def check_landscape(landscape, position):
    if landscape[position[0], position[1]] != 1:
        return True
    return False

def landscape_walker(steps, landscape, step_size=1, direction_set=("NORTH", "SOUTH", "EAST", "WEST")):
    """
    Normal random walker with step size 1
    :param n: number of steps
    :param step_size: defines the size of the steps
    :param x: empty numpy array consisting of n zeros
    :param y: empty numpy array consisting of n zeros
    :param direction_set: defines a set of directions, default values North, South, East, West
    :return: x, y numpy arrays
    """

    curr_pos = [33, 33]
    future_pos = [33, 33]
    check = False
    for step in range(1, steps):
        check = False
        while not check:
            direction = random.choice(direction_set)
            if direction == "EAST":
                future_pos[1] = curr_pos[1] + 1
                check = check_landscape(landscape, future_pos)
                if check:
                    landscape[future_pos[0], future_pos[1]] = 2
            elif direction == "WEST":
                future_pos[1] = curr_pos[1] - 1
                check = check_landscape(landscape, future_pos)
                if check:
                    landscape[future_pos[0], future_pos[1]] = 2
            elif direction == "NORTH":
                future_pos[0] = curr_pos[0] + 1
                check = check_landscape(landscape, future_pos)
                if check:
                    landscape[future_pos[0], future_pos[1]] = 2
            else:
                future_pos[0] = curr_pos[0] - 1
                check = check_landscape(landscape, future_pos)
                if check:
                    landscape[future_pos[0], future_pos[1]] = 2

        curr_pos = future_pos

    return landscape


def generate_area(landscape: bool, n: int, fill = 0.1):
    # old stuff
    x, y = np.zeros(n), np.zeros(n)
    if not landscape:
        return x, y

    # new stuff
    #TODO account for all fill points -> this method does not account for all
    arr = np.zeros((n, n))

    total_area = arr.size
    fill_area = int(total_area * fill)
    if fill_area % 2 == 1:
        fill_area += 1
    side_length = int(math.sqrt(fill_area))

    centre = n / 2

    # centre with x, y
    upper_left = (int(centre - side_length / 2), int(centre - side_length / 2))

    for x in range(side_length):
        for y in range(side_length):
            arr[upper_left[0] + y, upper_left[1] + x] = 1
    return arr


def some_other_walker():
    pass
    # maybe morsche neighbourhood
    #        y[pos] = y[pos - 1] - 1
    #return x, y


def multiple_walkers(x, y, steps, walkers, dif_start):
    xlist = []
    ylist = []
    for w in range(walkers):
        x_axis, y_axis = walker(x, y, steps, dif_start)
        xlist.append(x_axis)
        ylist.append(y_axis)
        x = np.zeros(steps)
        y = np.zeros(steps)
    return xlist, ylist


# plotting the walk
def plot_walkers(steps, walkers, xlist, ylist):
    """
    Generates plot of walker(s) and saves figure as PNG file.
    :param steps: Number of steps (needed for a figure title)
    :param walkers: Number of walkers (needed for a figure title)
    :param xlist: List of x-coordinates of walker(s) position
    :param ylist: List of y-coordinates of walker(s) position
    :return:
    """
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
    #TODO document everything in the README

    # defining the number of steps

    #landscape = generate_area(True, int(steps/100), 0.1)
    #walk = landscape_walker(int(steps/100), landscape)

    #plt.imshow(walk)
    #plt.show()

    # creating two array for containing x and y coordinate
    # of size equals to the number of size and filled up with 0's
    #x, y = generate_area(False, n)
    #step_size = 10
    # multiple walkers

    #walker(n, x, y, step_size)

    # x, y = fast_walker(n, x, y)
    #plot_walk(n, x, y)
    
    walkers, steps, dif_start = user_input()
    # creating two array for containing x and y coordinate
    # of size equals to the number of size and filled up with 0's
    x = np.zeros(steps)
    y = np.zeros(steps)

    # multiple walkers
    listX, listY = multiple_walkers(x, y, steps, walkers, dif_start)

    plot_walkers(steps, walkers, listX, listY)


if __name__ == "__main__":
    main()
