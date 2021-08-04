#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Random Walk Simulation """
import argparse
from typing import List
import matplotlib.pyplot as plt
import random_walker
from playground import Playground


def main(steps: int, walkers: int, save: bool, map_seed: int, land_scale: int,
         walker_types: List[str]):
    """
    Execute the random walker simulation for a given set of parameters

    :param steps: number of steps per walker
    :param walkers: number of walkers
    :param save: save the created figure
    :param map_seed: map seed for the playground
    :param land_scale: scale for the playground
    :param walker_types: specified walker types
    :return:
    """
    # Create Playground and walkers
    playground = Playground(seed=map_seed, scaling=land_scale)
    walker_list = random_walker.create_different_walkers(walkers, steps, walker_types)
    # Add Playground to plt
    plt.title("Random Walk ($n = " + str(steps) + "$ steps)")
    for x_positions, y_positions in playground.get_line_segments():
        plt.plot(x_positions, y_positions, color='red')
    # for each walker calculate the random walk and add to plt
    for walker_index in range(walkers):
        walker = walker_list[walker_index]
        walker.execute_random_walk(playground)
        # plotting the walk
        plt.plot(walker.x_positions,
                 walker.y_positions,
                 label=str(type(walker).__name__) + ' index: ' + str(walker_index))
    # optional save the plot
    if save:
        plt.savefig("./rand_walk_{}.png".format(steps))
    # show legend and plot
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # Parse Arguments
    parser = argparse.ArgumentParser(description='Executes and prints some random walkers')
    parser.add_argument('-w', '--walkers', type=int, default=3, help='number of walkers')
    parser.add_argument('-n', '--names', default=random_walker.get_walker_names(), nargs='+',
                        choices=random_walker.get_walker_names(),
                        help='space separated list of names of walker types to choose randomly')
    parser.add_argument('-ls', '--landscale', type=int, default=4, help='playground scale')
    parser.add_argument('-ps', '--playgroundseed', type=int, default=0,
                        choices=[0, 1, 2], help='map generation seed')
    parser.add_argument('-s', '--steps', type=int, default=100, help='number of steps per walker')
    parser.add_argument('--save', action="store_true", help='save figure')
    args = parser.parse_args()
    # Execute Main
    main(args.steps, args.walkers, args.save, args.playgroundseed, args.landscale, args.names)
