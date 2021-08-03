# -*- coding: utf-8 -*-
"""Base class unit for random walker"""
from enum import Enum
from math import sqrt
from typing import List, Union
import numpy as np
import random
from playground import Playground

"""constant for square root of 2"""
SQRT2 = sqrt(2)


class WalkDirection(Enum):
    """Enum Class with all possible walk directions"""
    Right = 1
    Left = 2
    Up = 3
    Down = 4
    UpRight = 5
    UpLeft = 6
    DownRight = 7
    DownLeft = 8

    def get_x_factor(self) -> float:
        """
        get the x amount of a walk direction

        :return: x amount
        """
        if self.name == 'Right':
            return 1
        elif self.name == 'Left':
            return -1
        elif self.name == 'Up' or self.name == 'Down':
            return 0
        elif self.name == 'UpRight' or self.name == 'DownRight':
            return SQRT2
        return -SQRT2

    def get_y_factor(self) -> float:
        """
        get the y amount of a walk direction

        :return: y amount
        """
        if self.name == 'Right' or self.name == 'Left':
            return 0
        elif self.name == 'Up':
            return 1
        elif self.name == 'Down':
            return -1
        elif self.name == 'UpRight' or self.name == 'UpLeft':
            return SQRT2
        return -SQRT2


class RandomWalker:
    """
    Base class for a random walker
    The possible walk directions and the step length
    can be changed by subclasses
    """
    def __init__(self, steps: int = 10000):
        """
        Create a new random walker

        :param steps: number of steps
        """
        # number of steps
        self.steps = steps
        # possible walk directions
        self.walkDirections: List[WalkDirection] = \
            [WalkDirection.Right, WalkDirection.Left, WalkDirection.Up, WalkDirection.Down]
        # positions at each step
        self.x_positions = np.zeros(self.steps, dtype=float)
        self.y_positions = np.zeros(self.steps, dtype=float)
        # default step length of the walker
        self.step_length = 1

    def get_random_walk_direction(self) -> WalkDirection:
        """
        Chooses a random WalkDirection from the walkDirections array

        :return: WalkDirection
        """
        return self.walkDirections[random.randint(0, len(self.walkDirections) - 1)]

    def get_walk_step_length(self, walk_direction: WalkDirection) -> Union[int, float]:
        """
        Calculates the step length for a given direction.
        Override in subclass in order to implement an other behaviour

        :param walk_direction: direction for this step
        :return: step length
        """
        return self.step_length

    def reset_position(self, index: int):
        """
        Reset the current position from index to the previous position

        :param index: current step
        :return: None
        """
        self.x_positions[index] = self.x_positions[index - 1]
        self.y_positions[index] = self.y_positions[index - 1]

    def calculate_position(self, index: int, playground: Playground):
        """
        Calculate the next position by randomly select a new walk direction
        and moving self.get_walk_step_length() in this direction.
        The position will be reset to the previous one if the position is outside the playground

        :param index: step index
        :param playground: Playground for the walker
        :return: None
        """
        walk_direction = self.get_random_walk_direction()
        self.x_positions[index] = \
            self.x_positions[index - 1] + walk_direction.get_x_factor() * self.get_walk_step_length(walk_direction)
        self.y_positions[index] = \
            self.y_positions[index - 1] + walk_direction.get_y_factor() * self.get_walk_step_length(walk_direction)
        if not playground.is_position_in_playground(self.x_positions[index], self.y_positions[index]):
            self.reset_position(index)

    def execute_random_walk(self, playground: Playground, start_x: int = 0, start_y: int = 0):
        """
        Execute the random walk calculation for all steps, starting at start_x, start_y on a playground

        :param playground: Playground for the walker
        :param start_x: start position x
        :param start_y: start position y
        :return: None
        """
        self.x_positions[0] = start_x
        self.y_positions[0] = start_y
        for index in range(1, self.steps):
            self.calculate_position(index, playground)


def create_different_walkers(count: int, steps: int) -> List[RandomWalker]:
    """
    Walker Factory creating random walkers which were inherited from the class RandomWalker

    :param count: number of walkers
    :param steps: steps for the walkers
    :return: Array of Walkers
    """
    result = []
    types = RandomWalker.__subclasses__()
    for i in range(count):
        random_type = types[random.randint(0, len(types) - 1)]
        random_object = random_type(steps)
        result.append(random_object)
    return result


class Rook(RandomWalker):
    """Rook Walker, can walk Up, Down, Left, Right, randomly 0 to 20 fields per step"""
    def __init__(self, *args):
        super().__init__(*args)

    def get_walk_step_length(self, walk_direction: WalkDirection) -> Union[int, float]:
        """Override base method to implement a random step length"""
        return random.randint(0, 20)


class King(RandomWalker):
    """King Walker, can walk in each directions, but only one field"""
    def __init__(self, *args):
        super().__init__(*args)
        self.walkDirections = [WalkDirection.DownLeft, WalkDirection.UpLeft, WalkDirection.DownRight,
                               WalkDirection.UpRight, WalkDirection.Up, WalkDirection.Down, WalkDirection.Right,
                               WalkDirection.Left]
        self.step_length = 1


class Bishop(RandomWalker):
    """Bishop Walker, can walk diagonal, using random step length between 0 and 20"""
    def __init__(self, *args):
        super().__init__(*args)
        self.walkDirections = [WalkDirection.DownLeft, WalkDirection.UpLeft, WalkDirection.DownRight, WalkDirection.UpRight]

    def get_walk_step_length(self, walk_direction: WalkDirection) -> Union[int, float]:
        """Override base method to implement a random step length"""
        return random.randint(0, 20)


class Queen(RandomWalker):
    """Queen Walker, can walk in each direction, using fixed step length of 20"""
    def __init__(self, *args):
        super().__init__(*args)
        self.walkDirections = [WalkDirection.DownLeft, WalkDirection.UpLeft, WalkDirection.DownRight, WalkDirection.UpRight, WalkDirection.Up, WalkDirection.Down, WalkDirection.Right, WalkDirection.Left]
        self.step_length = 20


class Pawn(RandomWalker):
    """Pawn Walker, can walk up or down including diagonals"""
    def __init__(self, *args):
        super().__init__(*args)
        if random.randint(0, 1) == 0:
            self.walkDirections = [WalkDirection.Up, WalkDirection.UpLeft, WalkDirection.UpRight]
        else:
            self.walkDirections = [WalkDirection.Down, WalkDirection.DownLeft, WalkDirection.DownRight]
        self.step_length = 1
