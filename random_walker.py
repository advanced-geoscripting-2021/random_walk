# -*- coding: utf-8 -*-
"""Base class unit for random walker"""
from enum import Enum
from math import sqrt
from typing import List, Union
import random
import numpy as np
from playground import Playground

# constant for square root of 2
SQRT2 = sqrt(2)


class WalkDirection(Enum):
    """Enum Class with all possible walk directions"""
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    UPRIGHT = 5
    UPLEFT = 6
    DOWNRIGHT = 7
    DOWNLEFT = 8

    def get_x_factor(self) -> float:
        """
        Get the x amount of a walk direction

        :return: x amount
        """
        if self.name == 'RIGHT':
            return 1
        if self.name == 'LEFT':
            return -1
        if self.name == 'UP' or self.name == 'DOWN':
            return 0
        if self.name == 'UPRIGHT' or self.name == 'DOWNRIGHT':
            return SQRT2
        return -SQRT2

    def get_y_factor(self) -> float:
        """
        Get the y amount of a walk direction

        :return: y amount
        """
        if self.name == 'RIGHT' or self.name == 'LEFT':
            return 0
        if self.name == 'UP':
            return 1
        if self.name == 'DOWN':
            return -1
        if self.name == 'UPRIGHT' or self.name == 'UPLEFT':
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
        self.walk_directions: List[WalkDirection] = \
            [WalkDirection.RIGHT, WalkDirection.LEFT, WalkDirection.UP, WalkDirection.DOWN]
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
        return self.walk_directions[random.randint(0, len(self.walk_directions) - 1)]

    def get_walk_step_length(self, walk_direction: WalkDirection) -> Union[int, float]:
        """
        Calculates the step length for a given direction.
        Override in subclass in order to implement an other behaviour

        :param walk_direction: direction for this step
        :return: step length
        """
        if walk_direction in self.walk_directions:
            return self.step_length
        return 0

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
        step_length = self.get_walk_step_length(walk_direction)
        self.x_positions[index] = \
            self.x_positions[index - 1] + \
            walk_direction.get_x_factor() * step_length
        self.y_positions[index] = \
            self.y_positions[index - 1] + \
            walk_direction.get_y_factor() * step_length
        if not playground.is_position_in_playground(self.x_positions[index],
                                                    self.y_positions[index]):
            self.reset_position(index)

    def execute_random_walk(self, playground: Playground, start_x: int = 0, start_y: int = 0):
        """
        Execute the random walk calculation for all steps, starting at start_x,
        start_y on a playground

        :param playground: Playground for the walker
        :param start_x: start position x
        :param start_y: start position y
        :return: None
        """
        self.x_positions[0] = start_x
        self.y_positions[0] = start_y
        for index in range(1, self.steps):
            self.calculate_position(index, playground)


def create_different_walkers(count: int, steps: int, walker_types: List[str]) -> List[RandomWalker]:
    """
    Walker Factory creating random walkers which were inherited from the class RandomWalker

    :param count: number of walkers
    :param steps: steps for the walkers
    :param walker_types: specify the possible walker types to choose
    :return: Array of Walkers
    """
    result = []
    # get subclasses from RandomWalker
    types = RandomWalker.__subclasses__()
    for _ in range(count):
        # pick random subclass
        random_type = types[random.randint(0, len(types) - 1)]
        while random_type.__name__ not in walker_types:
            random_type = types[random.randint(0, len(types) - 1)]
        # generate object
        random_object = random_type(steps)
        # add object to result array
        result.append(random_object)
    return result


def get_walker_names() -> List[str]:
    """
    Get all possible walker names from RandomWalker subclasses

    :return: List of Class Names
    """
    result = []
    # get subclasses from RandomWalker
    types = RandomWalker.__subclasses__()
    for class_type in types:
        result.append(class_type.__name__)
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
        self.walk_directions = [WalkDirection.DOWNLEFT, WalkDirection.UPLEFT,
                                WalkDirection.DOWNRIGHT, WalkDirection.UPRIGHT,
                                WalkDirection.UP, WalkDirection.DOWN,
                                WalkDirection.RIGHT, WalkDirection.LEFT]
        self.step_length = 1


class Bishop(RandomWalker):
    """Bishop Walker, can walk diagonal, using random step length between 0 and 20"""
    def __init__(self, *args):
        super().__init__(*args)
        self.walk_directions = [WalkDirection.DOWNLEFT, WalkDirection.UPLEFT,
                                WalkDirection.DOWNRIGHT, WalkDirection.UPRIGHT]

    def get_walk_step_length(self, walk_direction: WalkDirection) -> Union[int, float]:
        """Override base method to implement a random step length"""
        return random.randint(0, 20)


class Queen(RandomWalker):
    """Queen Walker, can walk in each direction, using fixed step length of 20"""
    def __init__(self, *args):
        super().__init__(*args)
        self.walk_directions = [WalkDirection.DOWNLEFT, WalkDirection.UPLEFT,
                                WalkDirection.DOWNRIGHT, WalkDirection.UPRIGHT,
                                WalkDirection.UP, WalkDirection.DOWN,
                                WalkDirection.RIGHT, WalkDirection.LEFT]
        self.step_length = 20


class Pawn(RandomWalker):
    """Pawn Walker, can walk up or down including diagonals"""
    def __init__(self, *args):
        super().__init__(*args)
        if random.randint(0, 1) == 0:
            self.walk_directions = [WalkDirection.UP, WalkDirection.UPLEFT,
                                    WalkDirection.UPRIGHT]
        else:
            self.walk_directions = [WalkDirection.DOWN, WalkDirection.DOWNLEFT,
                                    WalkDirection.DOWNRIGHT]
        self.step_length = 1
