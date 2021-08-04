#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Vectorized Walker"""


import matplotlib.pyplot as plt
import random
import numpy as np



def next_step(x, y, pos, direction, step_size):
    """ Returns the next step for a random walker"""
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
    elif direction == "SOUTH":
        x[pos] = x[pos - 1]
        y[pos] = y[pos - 1] - step_size
    # go northeast
    elif direction == "NORTHEAST":
        x[pos] = x[pos - 1] + step_size
        y[pos] = y[pos - 1] + step_size
    # go northwest
    elif direction == "NORTHWEST":
        x[pos] = x[pos - 1] - step_size
        y[pos] = y[pos - 1] + step_size
    # go southeast
    elif direction == "SOUTHEAST":
        x[pos] = x[pos - 1] + step_size
        y[pos] = y[pos - 1] - step_size
    # go southwest
    elif direction == "SOUTHWEST":
        x[pos] = x[pos - 1] - step_size
        y[pos] = y[pos - 1] - step_size
    return x, y


def different_start_pos(total_steps):
    """returns a tuple at a randomly selected position"""
    start_shift = int(total_steps / 100)
    return random.randint(-start_shift, start_shift)


def get_random_direction(direction_set):
    """Returns a random direction"""
    return random.choice(direction_set)


def create_walking_space(total_steps):
    # for random walker without landscape
    x, y = np.zeros(total_steps), np.zeros(total_steps)
    return x, y

def v_walker(x, y, total_steps, diff_start, step_size=1, mov_pattern=False):
    """
    Normal random walker with step size 1
    :param diff_start:
    :param total_steps: number of steps
    :param step_size: defines the size of the steps
    :param x: empty numpy array consisting of n zeros
    :param y: empty numpy array consisting of n zeros
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
        direction_set = ("NORTH", "SOUTH", "EAST", "WEST", "NORTHWEST", "NORTHEAST", "SOUTHWEST", "SOUTHEAST")

    # get random start position if that is wanted
    if diff_start is True:
        x[0] = different_start_pos(total_steps)
        y[0] = different_start_pos(total_steps)
    # for the total number of steps, calculate walker movement randomly
    for pos in range(1, total_steps):
        direction = get_random_direction(direction_set)
        x, y = next_step(x, y, pos, direction, step_size)
    return x, y


#TODO: implement multiple walkers for landscape walkers (and other possible walkers)
def multiple_v_walkers(x, y, total_steps, total_walkers, step_size, diff_start, mov_pattern):
    """
    Generates paths for multiple walkers
    :param x: np.array of x-coordinates (input: zeros)
    :param y: np.array of y-coordinates (input: zeros)
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
    for w in range(total_walkers):
        # call walker function to generate array of x and y coordinates of one walker
        x_axis, y_axis = v_walker(x, y, total_steps, diff_start, step_size, mov_pattern)
        # append to list
        x_list.append(x_axis)
        y_list.append(y_axis)
        # set input arrays back to zeros
        x = np.zeros(total_steps)
        y = np.zeros(total_steps)
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
