#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Vectorized Walker"""

import random
import math as m
import matplotlib.pyplot as plt
import numpy as np


def next_step(x_arr, y_arr, pos, direction, step_size):
    """
    Returns the next step for a random walker
    :param x_arr: numpy array of the walker's path – x-coordinates
    :param y_arr: numpy array of the walker's path – y-coordinates
    :param pos: which step is walker doing
    :param direction: direction of the step
    :param step_size: size of the step
    :return: updated arrays of the path
    """
    # go east
    if direction == "EAST":
        x_arr[pos] = x_arr[pos - 1] + step_size
        y_arr[pos] = y_arr[pos - 1]
    # go west
    elif direction == "WEST":
        x_arr[pos] = x_arr[pos - 1] - step_size
        y_arr[pos] = y_arr[pos - 1]
    # go north
    elif direction == "NORTH":
        x_arr[pos] = x_arr[pos - 1]
        y_arr[pos] = y_arr[pos - 1] + step_size
    # go south
    elif direction == "SOUTH":
        x_arr[pos] = x_arr[pos - 1]
        y_arr[pos] = y_arr[pos - 1] - step_size
    # go northeast
    elif direction == "NORTHEAST":
        x_arr[pos] = x_arr[pos - 1] + step_size
        y_arr[pos] = y_arr[pos - 1] + step_size
    # go northwest
    elif direction == "NORTHWEST":
        x_arr[pos] = x_arr[pos - 1] - step_size
        y_arr[pos] = y_arr[pos - 1] + step_size
    # go southeast
    elif direction == "SOUTHEAST":
        x_arr[pos] = x_arr[pos - 1] + step_size
        y_arr[pos] = y_arr[pos - 1] - step_size
    # go southwest
    elif direction == "SOUTHWEST":
        x_arr[pos] = x_arr[pos - 1] - step_size
        y_arr[pos] = y_arr[pos - 1] - step_size
    return x_arr, y_arr


def different_start_pos(total_steps):
    """
    Returns a random starting position of a walker
    :param total_steps: based on number of steps the start shift is chosen
    :return: tuple of random integer coordinates
    """
    if total_steps <= 10:
        start_shift = 10
    else:
        start_shift = int(m.sqrt(total_steps))
    return random.randint(-start_shift, start_shift), random.randint(-start_shift, start_shift)


def get_random_direction(direction_set):
    """
    Returns a random direction
    :param direction_set: von Neumann or Moor'sche neighborhood
    :return: random direction (f.e. 'NORTH')
    """
    return random.choice(direction_set)


def create_walking_space(total_steps):
    """
    Creating empty arrays for x,y-coordinates
    :param total_steps: number of steps
    :return: numpy arrays
    """
    # for random walker without landscape
    x_arr, y_arr = np.zeros(total_steps).astype(int), np.zeros(total_steps).astype(int)
    return x_arr, y_arr


def v_walker(x_arr, y_arr, total_steps, diff_start, step_size=1,
             mov_pattern=False):
    """
    Normal random walker with step size 1
    :param diff_start: if True, walker starts walking
           from a different position, else starts at (0,0)
    :param total_steps: number of steps
    :param step_size: defines the size of the steps
    :param x_arr: empty numpy array consisting of n zeros
    :param y_arr: empty numpy array consisting of n zeros
    :param mov_pattern: boolean, if True, Moor'sche neighboorhood is used, else Neumann
    :return: x, y numpy arrays
    """

    # checks which movement set the walker should get
    # Neumann or Moor
    if not mov_pattern:
        # von Neumann neighborhood
        direction_set = ("NORTH", "SOUTH", "EAST", "WEST")
    else:
        # Moor'sche neighborhood
        direction_set = ("NORTH", "SOUTH", "EAST", "WEST",
                         "NORTHWEST", "NORTHEAST", "SOUTHWEST", "SOUTHEAST")

    # get random start position if that is wanted
    if diff_start is True:
        start = (different_start_pos(total_steps))
    else:
        start = (0, 0)
    # for the total number of steps, calculate walker movement randomly
    for pos in range(1, total_steps):
        direction = get_random_direction(direction_set)
        x_arr, y_arr = next_step(x_arr, y_arr, pos, direction, step_size)
    return x_arr + start[0], y_arr + start[1]


def multiple_v_walkers(x_arr, y_arr, total_steps, total_walkers, step_size,
                       diff_start, mov_pattern):
    """
    Generates paths for multiple walkers
    :param x_arr: np.array of x-coordinates (input: zeros)
    :param y_arr: np.array of y-coordinates (input: zeros)
    :param total_steps: number of steps of individual walker
    :param total_walkers: number of walkers
    :param step_size: defines the size of the steps
    :param diff_start: bool value – if True, walkers start from different position
                                   if False, walkers start from the same position
    :param mov_pattern: boolean, if True, Moor'sche neighboorhood is used, else Neumann
    :return: lists of x and y coordinates
    """
    # create empty lists
    x_list = []
    y_list = []
    for _ in range(total_walkers):
        # call walker function to generate array of x and y coordinates of one walker
        x_axis, y_axis = v_walker(x_arr, y_arr, total_steps, diff_start, step_size, mov_pattern)
        # append to list
        x_list.append(x_axis)
        y_list.append(y_axis)
        # set input arrays back to zeros
        x_arr, y_arr = create_walking_space(total_steps)
    return x_list, y_list


# plotting the walk
def plot_v_walkers(total_steps, total_walkers, x_list, y_list):
    """
    Generates plot of walker(s) and saves figure as PNG file.
    :param total_steps: Number of steps (needed for a figure title)
    :param total_walkers: Number of walkers (needed for a figure title)
    :param x_list: List of x-coordinates of walker(s) position
    :param y_list: List of y-coordinates of walker(s) position
    :return: none
    """
    # set figure and axis
    fig = plt.figure(figsize=(5, 5), dpi=200)
    axes = fig.add_subplot(111)
    # create list of unique colors
    color = iter(plt.cm.rainbow(np.linspace(0, 1, total_walkers)))
    for wal in range(total_walkers):
        col = next(color)
        path_x = x_list[wal]
        path_y = y_list[wal]
        # plot vertices, path, start position and end position
        axes.scatter(path_x, path_y, color=col, alpha=0.25, s=1)
        axes.plot(path_x, path_y, color=col, alpha=0.25, lw=2, label='%s. walker' % (wal+1))
        axes.plot(path_x[0], path_y[0], color=col, marker='o')
        axes.plot(path_x[-1], path_y[-1], color=col, marker='+')
    axes.axis('equal')
    plt.xlabel('x')
    plt.ylabel('x')
    plt.legend()
    plt.tight_layout()
    plt.title("Random Walk (Number of walkers = " + str(total_walkers) +
              ", $n = " + str(total_steps) + "$ steps)")
    plt.savefig(".\\rand_walk_{}_{}.png".format(total_walkers, total_steps))
    plt.show()
