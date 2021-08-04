#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""__description__
"""

__author__ = "Christina Ludwig, GIScience Research Group, Heidelberg University"
__email__ = "christina.ludwig@uni-heidelberg.de"

import random


class Walker:

    def __init__(self, init_x=500, init_y=500):
        """
        Create walker object
        """
        self.x_coords = [init_x]
        self.y_coords = [init_y]

    def walk(self):
        """
        Walker walks one step forward in random direction
        :return:
        """
        last_x = self.x_coords[-1]
        last_y = self.y_coords[-1]
        new_x, new_y = self.nextStep(last_x, last_y)
        self.x_coords.append(new_x)
        self.y_coords.append(new_y)

    def nextStep(self, last_x, last_y):
        """
        Choose next position randomly
        :return:
        """
        val = random.randint(1, 4)
        if val == 1:
            new_x = last_x + 1
            new_y = last_y
        elif val == 2:
            new_x = last_x - 1
            new_y = last_y
        elif val == 3:
            new_x = last_x
            new_y = last_y + 1
        else:
            new_x = last_x
            new_y = last_y - 1
        return new_x, new_y
