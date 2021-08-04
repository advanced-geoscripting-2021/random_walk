"""Pytest Unit"""
import random_walker


def test_walk_direction_up():
    """Test Walk Direction handling"""
    assert random_walker.WalkDirection.UP.get_x_factor() == 0
    assert random_walker.WalkDirection.UP.get_y_factor() == 1


def test_walk_direction_down():
    """Test Walk Direction handling"""
    assert random_walker.WalkDirection.DOWN.get_x_factor() == 0
    assert random_walker.WalkDirection.DOWN.get_y_factor() == -1


def test_walk_direction_left():
    """Test Walk Direction handling"""
    assert random_walker.WalkDirection.LEFT.get_x_factor() == -1
    assert random_walker.WalkDirection.LEFT.get_y_factor() == 0


def test_walk_direction_right():
    """Test Walk Direction handling"""
    assert random_walker.WalkDirection.RIGHT.get_x_factor() == 1
    assert random_walker.WalkDirection.RIGHT.get_y_factor() == 0


def test_walk_direction_up_left():
    """Test Walk Direction handling"""
    assert random_walker.WalkDirection.UPLEFT.get_x_factor() == -random_walker.SQRT2
    assert random_walker.WalkDirection.UPLEFT.get_y_factor() == random_walker.SQRT2


def test_walk_direction_up_right():
    """Test Walk Direction handling"""
    assert random_walker.WalkDirection.UPRIGHT.get_x_factor() == random_walker.SQRT2
    assert random_walker.WalkDirection.UPRIGHT.get_y_factor() == random_walker.SQRT2


def test_walk_direction_down_right():
    """Test Walk Direction handling"""
    assert random_walker.WalkDirection.DOWNRIGHT.get_x_factor() == random_walker.SQRT2
    assert random_walker.WalkDirection.DOWNRIGHT.get_y_factor() == -random_walker.SQRT2


def test_walk_direction_down_left():
    """Test Walk Direction handling"""
    assert random_walker.WalkDirection.DOWNLEFT.get_x_factor() == -random_walker.SQRT2
    assert random_walker.WalkDirection.DOWNLEFT.get_y_factor() == -random_walker.SQRT2
