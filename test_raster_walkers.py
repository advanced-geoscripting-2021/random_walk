#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" tests the raster_walker.py functionality"""


import numpy as np
import raster_walker as rw


def test_create_raster():
    """ Checks if raster creation works and implements the obstacle correctly """
    created_raster = rw.create_raster(100)
    expected_raster = np.zeros((10, 10))
    expected_raster[3:6, 3:6] = 1
    assert np.array_equal(created_raster, expected_raster)


def test_raster_one_step():
    """ Checks if raster one step returns the correct changes """
    direction_set = ("NORTH", "SOUTH", "EAST", "WEST")
    curr_pos = [0, 0]
    future_pos = [0, 0]

    pos_north = rw.raster_one_step(direction_set[0], curr_pos, future_pos)
    future_pos = [0, 0]
    pos_south = rw.raster_one_step(direction_set[1], curr_pos, future_pos)
    future_pos = [0, 0]
    pos_east = rw.raster_one_step(direction_set[2], curr_pos, future_pos)
    future_pos = [0, 0]
    pos_west = rw.raster_one_step(direction_set[3], curr_pos, future_pos)

    expected_north = [1, 0]
    expected_south = [-1, 0]
    expected_east = [0, 1]
    expected_west = [0, -1]

    assert pos_north == expected_north
    assert pos_south == expected_south
    assert pos_east == expected_east
    assert pos_west == expected_west


def test_check_landscape():
    """ Checks if raster obstacle check is working correct """

    raster = np.zeros((4, 4))
    raster[1:3, 1:3] = 1
    raster[3, 3] = 3
    position1 = [0, 0]
    position2 = [2, 2]
    position3 = [0, -1]
    position4 = [-1, 0]
    position5 = [4, 0]
    position6 = [0, 4]
    position7 = [3, 3]

    assert rw.check_landscape(raster, position1) is True
    assert rw.check_landscape(raster, position2) is False
    assert rw.check_landscape(raster, position3) is True
    assert rw.check_landscape(raster, position4) is True
    assert rw.check_landscape(raster, position5) is True
    assert rw.check_landscape(raster, position6) is True
    assert rw.check_landscape(raster, position7) is False


if __name__ == "__main__":
    test_raster_one_step()
    test_create_raster()
    test_check_landscape()
