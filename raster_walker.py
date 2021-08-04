#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Rasterized Walker"""

import matplotlib.pyplot as plt
import random
import numpy as np
import math


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


def r_walker(landscape, total_steps, step_size=1, direction_set=("NORTH", "SOUTH", "EAST", "WEST")):
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


def create_raster(n: int, fill=0.1):
    """
    generates x,y 1D arrays with zeros for total_steps or
    generates landscape 2D array with obstacles if landscape is true
    :param landscape: 2D numpy array with some landscape features
    :param n: length of arrays or size of dimensions (2D)
    :param fill: how much of the area of the 2D array shall be filled with obstacles (percentage)
    :return:
    """

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


def plot_raster(arr):
    """
    Plots landscape
    :param arr: raster array of landscape
    :return:
    """
    #TODO could be do with some more adjustements
    plt.imshow(arr)
    plt.show()
