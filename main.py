#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Random Walk Simulation """

# Python code for 2D random walk.
# Source: https://www.geeksforgeeks.org/random-walk-implementation-python/
import matplotlib.pyplot as plt
from matplotlib import cm
import random
import numpy as np
import math
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
    run_random_walkers(total_steps, total_walkers, step_size, landscape, start_point)


# def user_input():
#    try:
#        walkers = int(sys.argv[1])
#        steps = int(sys.argv[2])
#        dif_start = bool(int(sys.argv[3]))
#    except Exception as err:
#        print("Incorrect input: ", err)
#        sys.exit()
#    return walkers, steps, dif_start


def walker(x, y, total_steps, diff_start, step_size=1, direction_set=("NORTH", "SOUTH", "EAST", "WEST")):
    """
    Normal random walker with step size 1
    :param diff_start:
    :param total_steps: number of steps
    :param step_size: defines the size of the steps
    :param x: empty numpy array consisting of n zeros
    :param y: empty numpy array consisting of n zeros
    :param direction_set: defines a set of directions, default values North, South, East, West
    :return: x, y numpy arrays
    """

    if diff_start is True:
        x[0] = random.randint(-total_steps / 100, total_steps / 100)
        y[0] = random.randint(-total_steps / 100, total_steps / 100)
    for pos in range(1, total_steps):
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


def landscape_walker(landscape, total_steps, step_size=1, direction_set=("NORTH", "SOUTH", "EAST", "WEST")):
    """
    Normal random walker with step size 1
    :param total_steps: integer specifying the number of steps by the walker
    :param landscape: 2D numpy array with some landscape features
    :param step_size: defines the size of the steps
    :param direction_set: defines a set of directions, default values North, South, East, West
    :return: x, y numpy arrays
    """
 
    # TODO: ADJUST IT dynamically
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


def generate_area(landscape: bool, n: int, fill=0.1):
    """
    generates x,y 1D arrays with zeros for total_steps or
    generates landscape 2D array with obstacles if landscape is true
    :param landscape: 2D numpy array with some landscape features
    :param n: length of arrays or size of dimensions (2D)
    :param fill: how much of the area of the 2D array shall be filled with obstacles (percentage)
    :return:
    """
    # for random walker without landscape
    x, y = np.zeros(n), np.zeros(n)
    if not landscape:
        return x, y

    arr = np.zeros((n, n))

    total_area = arr.size
    fill_area = int(total_area * fill)
    if fill_area % 2 == 1:
        fill_area += 1
    side_length = int(math.sqrt(fill_area))

    centre = n / 2

    # centre with x, y
    upper_left = (int(centre - side_length / 2), int(centre - side_length / 2))

    # places an obstacle as square in the middle of the landscape
    for x in range(side_length):
        for y in range(side_length):
            arr[upper_left[0] + y, upper_left[1] + x] = 1
    return arr


def some_other_walker():
    pass
    # maybe morsche neighbourhood


#TODO: implement multiple walkers for landscape walkers (and other possible walkers)
def multiple_walkers(x, y, total_steps, total_walkers, step_size, diff_start):
    """
    Generates paths for multiple walkers
    :param x: np.array of x-coordinates (input: zeros)
    :param y: np.array of y-coordinates (input: zeros)
    :param total_steps: number of steps of individual walker
    :param total_walkers: number of walkers
    :param step_size: defines the size of the steps
    :param diff_start: bool value – if True, walkers start from different position
                                   if False, walkers start from the same position
    :return: lists of x and y coordinates
    """
    # create empty lists
    x_list = []
    y_list = []
    for w in range(total_walkers):
        # call walker function to generate array of x and y coordinates of one walker
        x_axis, y_axis = walker(x, y, total_steps, diff_start, step_size, )
        # append to list
        x_list.append(x_axis)
        y_list.append(y_axis)
        # set input arrays back to zeros
        x = np.zeros(total_steps)
        y = np.zeros(total_steps)
    return x_list, y_list


# plotting the walk
def plot_walkers(total_steps, total_walkers, x_list, y_list):
    """
    Generates plot of walker(s) and saves figure as PNG file.
    :param total_steps: Number of steps (needed for a figure title)
    :param total_walkers: Number of walkers (needed for a figure title)
    :param x_list: List of x-coordinates of walker(s) position
    :param y_list: List of y-coordinates of walker(s) position
    :return: none
    """
    # set figure and axis
    fig = plt.figure(figsize=(8, 8), dpi=200)
    ax = fig.add_subplot(111)
    # create list of unique colors
    color = iter(plt.cm.rainbow(np.linspace(0, 1, total_walkers)))
    for w in range(total_walkers):
        c = next(color)
        path_x = x_list[w]
        path_y = y_list[w]
        # plot vertices, path, start position and end position
        ax.scatter(path_x, path_y, color=c, alpha=0.25, s=1)
        ax.plot(path_x, path_y, color=c, alpha=0.25, lw=2, label='%s. walker' % (w+1))
        ax.plot(path_x[0], path_y[0], color=c, marker='o')
        ax.plot(path_x[-1], path_y[-1], color=c, marker='+')
    plt.legend()
    plt.title("Random Walk (Number of walkers = " + str(total_walkers) + ", $n = " + str(total_steps) + "$ steps)")
    plt.savefig(".\\rand_walk_{}_{}.png".format(total_walkers, total_steps))
    plt.show()


def plot_raster(arr):
    """
    Plots landscape
    :param arr: raster array of landscape
    :return:
    """
    #TODO could be do with some more adjustements
    plt.imshow(arr)
    plt.show()


def run_random_walkers(total_steps, total_walkers, step_size, landscape, diff_start):
    """
    executes the random walker tool based on input data
    :param total_steps: number of total steps of the random walker
    :param total_walkers: number of walkers
    :param step_size: step size for each step
    :param landscape: boolean, if True, 2D area with obstacles is generated as base layer
    :param diff_start: boolean, if True, different start points for each walker
    :return:
    """
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
        list_x, list_y = multiple_walkers(x, y, total_steps, total_walkers, step_size, diff_start)
        plot_walkers(total_steps, total_walkers, list_x, list_y)


if __name__ == "__main__":
    run_random_walkers(10000, 5, 1, False, True)
