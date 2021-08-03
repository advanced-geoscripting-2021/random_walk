#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Random Walk Simulation """

# Python code for 2D random walk.
# Source: https://www.geeksforgeeks.org/random-walk-implementation-python/
import numpy
import matplotlib.pyplot as plt
import random
import argparse
import random_walker
from playground import Playground


COLORS = ['blue', 'orange', 'green', 'red', 'purple']


def main(steps: int, walkers: int, save: bool):
    playground = Playground(seed=1)
    walker_list = random_walker.create_different_walkers(walkers, steps)
    plt.title("Random Walk ($n = " + str(steps) + "$ steps)")
    for x, y in playground.get_line_segments():
        plt.plot(x, y, color='red')

    for walker_index in range(walkers):
        walker = walker_list[walker_index]
        walker.execute_random_walk(playground)
        # plotting the walk
        plt.plot(walker.x_positions, walker.y_positions, label=str(type(walker).__name__) +' index: ' + str(walker_index))
    if save:
        plt.savefig("./rand_walk_{}.png".format(steps))
    plt.legend()
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Executes and prints some random walkers')
    parser.add_argument('-s', '--steps', type=int, default=10000, help='number of steps per walker')
    parser.add_argument('-w', '--walkers', type=int, default=1, help='number of walkers')
    parser.add_argument('--save', action="store_true", help='save figure')
    args = parser.parse_args()
    main(args.steps, args.walkers, args.save)
