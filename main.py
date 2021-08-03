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
@click.option('--verbose', is_flag=False, help="Will print verbose messages.")
def cli(verbose: bool) -> None:
    if verbose:
        click.echo("We are in the verbose mode.")
    click.echo("Hello World, inside the cli function")


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


def walker(n, x, y, step_size=1, direction_set=("NORTH", "SOUTH", "EAST", "WEST")):
    """
    Normal random walker with step size 1
    :param n: number of steps
    :param step_size: defines the size of the steps
    :param x: empty numpy array consisting of n zeros
    :param y: empty numpy array consisting of n zeros
    :param direction_set: defines a set of directions, default values North, South, East, West
    :return: x, y numpy arrays
    """

    for pos in range(1, n):
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

def landscape_walker(n, landscape, step_size=1, direction_set=("NORTH", "SOUTH", "EAST", "WEST")):
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
    for step in range(1, n):
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
    # maybe morsche neighbourhood
    pass


# plotting the walk
def plot_walk(n, x, y):
    plt.title("Random Walk ($n = " + str(n) + "$ steps)")
    plt.plot(x, y)
    # plt.savefig("./rand_walk_{}.png".format(n))
    plt.show()

def plot_raster(arr):
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
    main()
