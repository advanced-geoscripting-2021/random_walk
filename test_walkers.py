import raster_walker as rw
import vector_walkers as vw
import numpy as np


def test_create_raster():
    """ Test if raster creation works and implements the obstacle correctly """
    created_raster = rw.create_raster(100)
    expected_raster = np.zeros((10, 10))
    expected_raster[3:6, 3:6] = 1
    assert np.array_equal(created_raster, expected_raster)

# def test_walker():
#     created_raster = rw.create_raster(100)
#     walk = rw.r_walker(100, created_raster)
#     rw.plot_raster(walk, 100)


def test_raster_one_step():
    direction_set = ("NORTH", "SOUTH", "EAST", "WEST")
    curr_pos = [0, 0]
    future_pos = [0, 0]

    pos_north = rw.raster_one_step(direction_set[0], curr_pos, future_pos)
    pos_south = rw.raster_one_step(direction_set[1], curr_pos, future_pos)
    pos_east = rw.raster_one_step(direction_set[2], curr_pos, future_pos)
    pos_west = rw.raster_one_step(direction_set[3], curr_pos, future_pos)

    expected_north = [1, 0]
    expected_south = [-1, 0]
    expected_east = [0, 1]
    expected_west = [0, -1]

    assert pos_north == expected_north
    assert pos_south == expected_south
    assert pos_east == expected_east
    assert pos_west == expected_west


test_raster_one_step()
test_walker()