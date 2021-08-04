#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Random Walk Simulation """

# Python code for 2D random walk.
# Source: https://www.geeksforgeeks.org/random-walk-implementation-python/

import click
import raster_walker as rw
import vector_walkers as vw


# user input – click
_total_steps_option = [
    click.option(
        "--total_steps",
        "-ts",
        default=10000,
        type=int,
        help="Specify the number of total steps for each random walker, Default is 10,000, Minimum 100",
    )
]

_total_walkers_option = [
    click.option(
        "--total_walkers",
        "-tw",
        default=1,
        type=int,
        help="Specify the number of total walkers, Default is 1, Minimum is 1",
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

_mov_pattern_option = [
    click.option(
        "--mov_pattern",
        "-mp",
        default=False,
        type=bool,
        help="Specify the neighborhood movement pattern, False is Neumann, True is Moor",
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
@add_options(_mov_pattern_option)
def run(
        total_steps: int,
        total_walkers: int,
        step_size: int,
        landscape: bool,
        start_point: bool,
) -> None:
    """ execute command to generate random walkers """
    run_random_walkers(total_steps, total_walkers, step_size, landscape, start_point)


def run_random_walkers(total_steps, total_walkers, step_size, landscape, diff_start, mov_pattern):
    """
    executes the random walker tool based on input data
    :param total_steps: number of total steps of the random walker
    :param total_walkers: number of walkers
    :param step_size: step size for each step
    :param landscape: boolean, if True, 2D area with obstacles is generated as base layer
    :param diff_start: boolean, if True, different start points for each walker
    :param mov_pattern: boolean, if True, Moor'sche neighboorhood is used, else Neumann
    :return:
    """

    # adjust wrong input, quick but powerful!;)
    if total_steps < 100:
        total_steps = 100
    if total_walkers < 1:
        total_walkers = 1

    # diverted because of the completely different implementation methods -> could be done better in the future
    if landscape:
        # percentage of how much space obstacles shall block
        fill_percentage = 0.1
        landscape_raster = rw.create_raster(total_steps, fill_percentage)
        walk = rw.r_walker(total_steps, landscape_raster)
        # plot landscape raster with obstacles and walker
        rw.plot_raster(walk, total_steps)
    else:
        # creating two arrays for containing x and y coordinate
        # of size equals to the number of size and filled up with 0's
        x, y = vw.create_walking_space(total_steps)

        # multiple walkers
        list_x, list_y = vw.multiple_v_walkers(x, y, total_steps, total_walkers, step_size, diff_start, mov_pattern)
        vw.plot_v_walkers(total_steps, total_walkers, list_x, list_y)


if __name__ == "__main__":
    run_random_walkers(10, 5, 1, True, True, True)
