#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Rasterized Walker"""

import matplotlib.pyplot as plt
import random
import numpy as np
import math
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch


def check_landscape(landscape, position):
    """
    Checks if next position of walker intersects given landscape
    :param landscape:
    :param position:
    :return:
    """
    # implement endless border -> reach border on the right, come in on the left
    # like the good old snake
    if abs(position[0]) >= landscape.shape[0]:
        position[0] = position[0] % landscape.shape[0]
    if abs(position[1]) >= landscape.shape[1]:
        position[1] = position[1] % landscape.shape[1]

    # check if the given position is an obstacle or the starting point
    if landscape[position[0], position[1]] != 1 and landscape[position[0], position[1]] != 3:
        return True
    return False


def raster_one_step(direction, curr_pos, future_pos):
    if direction == "EAST":
        future_pos[1] = curr_pos[1] + 1
    elif direction == "WEST":
        future_pos[1] = curr_pos[1] - 1
    elif direction == "NORTH":
        future_pos[0] = curr_pos[0] + 1
    else:
        future_pos[0] = curr_pos[0] - 1

    return future_pos


def r_walker(total_steps, landscape, direction_set=("NORTH", "SOUTH", "EAST", "WEST")):
    """
    Random walker on 2D array with an obstacle with step size 1
    :param total_steps: integer specifying the number of steps by the walker
    :param landscape: 2D numpy array with some landscape features
    :param direction_set: defines a set of directions, default values North, South, East, West
    :return: x, y numpy arrays
    """

    # start upper left corner
    curr_pos = [0, 0]
    future_pos = [0, 0]

    # give the starting position another value for plotting it later
    landscape[curr_pos[0], curr_pos[1]] = 3

    for step in range(0, total_steps):

        check = False

        while not check:
            direction = random.choice(direction_set)
            future_pos = raster_one_step(direction, curr_pos, future_pos)
            check = check_landscape(landscape, future_pos)

        landscape[future_pos[0], future_pos[1]] = 2
        curr_pos = future_pos
    return landscape


def create_raster(total_steps: int, fill=0.1):
    """
    generates x,y 1D arrays with zeros for total_steps or
    generates landscape 2D array with obstacles if landscape is true
    :param total_steps: total count of steps
    :param fill: how much of the area of the 2D array shall be filled with obstacles (percentage)
    :return:
    """

    # side_length as square root of the total steps
    side_length = int(math.sqrt(total_steps))

    # create 2D array
    arr = np.zeros((side_length, side_length))

    total_area = arr.size
    fill_area = int(total_area * fill)
    if fill_area % 2 == 1:
        fill_area += 1

    # get length of one size of the square
    side_length_obstacle = int(math.sqrt(fill_area))

    centre = side_length / 2

    # centre with x, y
    upper_left = (int(centre - side_length_obstacle / 2), int(centre - side_length_obstacle / 2))

    # places an obstacle as square in the middle of the landscape arr
    for x in range(side_length_obstacle):
        for y in range(side_length_obstacle):
            arr[upper_left[0] + y, upper_left[1] + x] = 1
    return arr


def plot_raster(arr, total_steps):
    """
    Plots landscape with the path of the random walker
    :param total_steps: total number of steps
    :param arr: raster array of landscape
    :return:
    """
    cmap = ListedColormap(["grey", "black", "darkgreen", "red"])

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.imshow(arr, cmap=cmap,)

    ax.set_title("Random Walk (Number of walkers = 1, total steps: " + str(total_steps))

    # Add a legend for labels
    legend_labels = {"black": "obstacle", "darkgreen": "path", "red": "start point"}

    patches = [Patch(color=color, label=label)
               for color, label in legend_labels.items()]

    ax.legend(handles=patches,
              bbox_to_anchor=(1.35, 1),
              facecolor="white")

    ax.set_axis_off()
    plt.show()
