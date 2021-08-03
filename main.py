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
import click

# user input – click
_total_steps_option = [
    click.option(
        "--total_steps",
        "-ts",
        default=10000,
        type=int,
        help="Specify the number of total steps for the random walker, Default is 10,000",
    )
]

_total_walkers_option = [
    click.option(
        "--total_walkers",
        "-tw",
        default=1,
        type=int,
        help="Specify the number of total walkers, Default is 1",
    )
]

_step_size_option = [
    click.option(
        "--step_size",
        "-ss",
        default=1,
        type=int,
        help="Specify the size of the steps taken, Default is 1",
    )
]

_landscape_option = [
    click.option(
        "--landscape",
        "-l",
        default=False,
        type=bool,
        help="Specify whether a grid landscape exists as base layer or not, Default is False",
    )
]

_start_point_option = [
    click.option(
        "--start_point",
        "-sp",
        default=False,
        type=bool,
        help="Specify whether the walkers shall start from the same point or not, Default is False",
    )
]


def add_options(options):
    """Functions adds options to cli."""

    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func

    return _add_options


@click.group()
@click.option('--verbose', '-v', is_flag=False, help="Will print verbose messages.")
def cli(verbose: bool) -> None:
    if verbose:
        click.echo("We are in the verbose mode. Which does not make any difference right now.. but hey, have fun!")


@cli.command()
@add_options(_total_steps_option)
@add_options(_total_walkers_option)
@add_options(_step_size_option)
@add_options(_landscape_option)
@add_options(_start_point_option)
def run(
        total_steps: int,
        total_walkers: int,
        step_size: int,
        landscape: bool,
        start_point: bool,
) -> None:
    """ execute command to generate random walkers """
    main_clicks(total_steps, total_walkers, step_size, landscape, start_point)


# def user_input():
#    try:
#        walkers = int(sys.argv[1])
#        steps = int(sys.argv[2])
#        dif_start = bool(int(sys.argv[3]))
#    except Exception as err:
#        print("Incorrect input: ", err)
#        sys.exit()
#    return walkers, steps, dif_start


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
        x[0] = random.randint(-steps/10, steps/10)
        y[0] = random.randint(-steps/10, steps/10)
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
    """
    Checks if next position of walker intersects given landscape
    :param landscape:
    :param position:
    :return:
    """
    if landscape[position[0], position[1]] != 1:
        return True
    return False


def landscape_walker(total_steps, landscape, step_size=1, direction_set=("NORTH", "SOUTH", "EAST", "WEST")):
    """
    Normal random walker with step size 1
    :param n: number of steps
    :param step_size: defines the size of the steps
    :param x: empty numpy array consisting of n zeros
    :param y: empty numpy array consisting of n zeros
    :param direction_set: defines a set of directions, default values North, South, East, West
    :return: x, y numpy arrays
    """
 
    # TODO: ADJUST IT
    curr_pos = [33, 33]
    future_pos = [33, 33]

    for step in range(0, total_steps):
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
    # for random walker without landscape
    x, y = np.zeros(n), np.zeros(n)
    if not landscape:
        return x, y

    # random walker with landscape

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

    # place a polygon in the middle of the landscape
    for x in range(side_length):
        for y in range(side_length):
            arr[upper_left[0] + y, upper_left[1] + x] = 1
    return arr


def some_other_walker():
    pass
    # maybe morsche neighbourhood
    #        y[pos] = y[pos - 1] - 1
    #return x, y


#TODO: implement multiple walkers for landscape walkers (and other possible walkers)
def multiple_walkers(x, y, steps, walkers, dif_start):
    """
    Generates paths for multiple walkers
    :param x: np.array of x-coordinates (input: zeros)
    :param y: np.array of y-coordinates (input: zeros)
    :param steps: number of steps of individual walker
    :param walkers: number of walkers
    :param dif_start: bool value – if True, walkers start from different position
                                   if False, walkers start from the same position
    :return: lists of x and y coordinates
    """
    # create empty lists
    xlist = []
    ylist = []
    for w in range(walkers):
        # call walker function to generate array of x and y coordinates of one walker
        x_axis, y_axis = walker(x, y, steps, dif_start)
        # append to list
        xlist.append(x_axis)
        ylist.append(y_axis)
        # set input arrays back to zeros
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
    :return: none
    """
    # set figure and axis
    fig = plt.figure(figsize=(8,8), dpi=200)
    ax = fig.add_subplot(111)
    # create list of unique colors
    color = iter(plt.cm.rainbow(np.linspace(0, 1, walkers)))
    for w in range(walkers):
        c = next(color)
        pathX = xlist[w]
        pathY = ylist[w]
        # plot vertices, path, start position and end position
        ax.scatter(pathX, pathY, color=c, alpha=0.25, s=1)
        ax.plot(pathX, pathY, color=c, alpha=0.25, lw=2, label='%s. walker' % (w+1))
        ax.plot(pathX[0],pathY[0], color=c, marker='o')
        ax.plot(pathX[-1], pathY[-1], color=c, marker='+')
    plt.legend()
    plt.title("Random Walk (Number of walkers = " + str(walkers) + ", $n = " + str(steps) + "$ steps)")
    plt.savefig(".\\rand_walk_{}_{}.png".format(walkers, steps))
    plt.show()


def plot_raster(arr):
    """
    Plots landscape
    :param arr: raster array of landscape
    :return:
    """
    plt.imshow(arr)
    plt.show()


def main():
    #TODO document everything in the README
    total_steps = 10000
    total_walkers = 1
    step_size = 1

    landscape = generate_area(True, int(total_steps/100), 0.1)
    walk = landscape_walker(int(total_steps/100), landscape)

    # plot landscape raster with obstacles and walker
    plot_raster(walk)

    # creating two array for containing x and y coordinate
    # of size equals to the number of size and filled up with 0's
    x, y = generate_area(False, total_steps)
    step_size = 10
    # multiple walkers

    walker(total_steps, x, y, step_size)
    # x, y = fast_walker(n, x, y)
    plot_walk(total_steps, x, y)
    
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



def main_clicks(total_steps, total_walkers, step_size, landscape, start_point):
    # diverted because of the completely different implementation methods -> could be done better in the future
    if landscape:
        fill_percentage = 0.1
        landscape_raster = generate_area(landscape, int(total_steps/100), fill_percentage)
        walk = landscape_walker(int(total_steps/100), landscape_raster)
        # plot landscape raster with obstacles and walker
        plot_raster(walk)
    else:
        # creating two arrays for containing x and y coordinate
        # of size equals to the number of size and filled up with 0's
        x, y = generate_area(landscape, total_steps)

        # multiple walkers

        walker(total_steps, x, y, step_size)
        plot_walk(total_steps, x, y)


if __name__ == "__main__":
    # main()
    main_clicks(10000, 1, 1, False, False)
