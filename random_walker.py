from enum import Enum
from math import sqrt
from typing import List, Union
import numpy as np
import random
from playground import Playground

SQRT2 = sqrt(2)


class WalkDirection(Enum):
    Right = 1
    Left = 2
    Up = 3
    Down = 4
    UpRight = 5
    UpLeft = 6
    DownRight = 7
    DownLeft = 8

    def get_x_factor(self):
        if self.name == 'Right':
            return 1
        elif self.name == 'Left':
            return -1
        elif self.name == 'Up' or self.name == 'Down':
            return 0
        elif self.name == 'UpRight' or self.name == 'DownRight':
            return SQRT2
        return -SQRT2

    def get_y_factor(self):
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
    def __init__(self, steps: int = 10000):
        self.steps = steps
        self.walkDirections: List[WalkDirection] = [WalkDirection.Right, WalkDirection.Left, WalkDirection.Up, WalkDirection.Down]
        self.x_positions = np.zeros(self.steps, dtype=float)
        self.y_positions = np.zeros(self.steps, dtype=float)
        self.step_length = 1

    def get_random_walk_direction(self) -> WalkDirection:
        return self.walkDirections[random.randint(0, len(self.walkDirections) - 1)]

    def get_walk_step_length(self, walk_direction: WalkDirection) -> Union[int, float]:
        return self.step_length

    def reset_position(self, index: int):
        self.x_positions[index] = self.x_positions[index - 1]
        self.y_positions[index] = self.y_positions[index - 1]

    def calculate_position(self, index: int, playground: Playground):
        walk_direction = self.get_random_walk_direction()
        self.x_positions[index] = \
            self.x_positions[index - 1] + walk_direction.get_x_factor() * self.get_walk_step_length(walk_direction)
        self.y_positions[index] = \
            self.y_positions[index - 1] + walk_direction.get_y_factor() * self.get_walk_step_length(walk_direction)
        if not playground.is_position_in_playground(self.x_positions[index], self.y_positions[index]):
            self.reset_position(index)

    def execute_random_walk(self, playground: Playground, start_x: int = 0, start_y: int = 0):
        self.x_positions[0] = start_x
        self.y_positions[0] = start_y
        for index in range(1, self.steps):
            self.calculate_position(index, playground)


def create_different_walkers(count: int, steps: int):
    result = []
    types = RandomWalker.__subclasses__()
    print(types)
    for i in range(count):
        random_type = types[random.randint(0, len(types) - 1)]
        random_object = random_type(steps)
        result.append(random_object)
    return result


class Rook(RandomWalker):
    def __init__(self, *args):
        super().__init__(*args)

    def get_walk_step_length(self, walk_direction: WalkDirection) -> Union[int, float]:
        return random.randint(0, 20)


class King(RandomWalker):
    def __init__(self, *args):
        super().__init__(*args)


class Bishop(RandomWalker):
    def __init__(self, *args):
        super().__init__(*args)
        self.walkDirections = [WalkDirection.DownLeft, WalkDirection.UpLeft, WalkDirection.DownRight, WalkDirection.UpRight]

    def get_walk_step_length(self, walk_direction: WalkDirection) -> Union[int, float]:
        return random.randint(0, 20)


class Queen(RandomWalker):
    def __init__(self, *args):
        super().__init__(*args)
        self.walkDirections = [WalkDirection.DownLeft, WalkDirection.UpLeft, WalkDirection.DownRight, WalkDirection.UpRight, WalkDirection.Up, WalkDirection.Down, WalkDirection.Right, WalkDirection.Left]
        self.step_length = 20


class Pawn(RandomWalker):
    def __init__(self, *args):
        super().__init__(*args)
        if random.randint(0, 1) == 0:
            self.walkDirections = [WalkDirection.Up, WalkDirection.UpLeft, WalkDirection.UpRight]
        else:
            self.walkDirections = [WalkDirection.Down, WalkDirection.DownLeft, WalkDirection.DownRight]
