#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Unit testing of walkers"""

import raster_walker as rw
import vector_walker as vw


def test_walker_next():
    # define initial position and direction
    start = (2, 2)
    total_steps = 1
    x, y = vw.create_walking_space(total_steps)
    direction = "EAST"
    step_size = 1
    expected_new_x = 3
    expected_new_y = 2

    # execute the nextstep function
    new_x, new_y = vw.next_step(x, y, 0, direction, step_size)


    # assert
    assert new_x[0] + start[0] == expected_new_x
    assert new_y[0] + start[1] == expected_new_y
