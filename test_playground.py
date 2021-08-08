"""Pytest Unit"""
from playground import Playground
from shapely.geometry import Polygon

def test_standard_constructor():
    """Calling the standard constructor with default inputs to test the class setter-functions"""
    playground_obj = Playground(scaling=1, x_max=250, y_max=250, seed=0)
    assert playground_obj.x_max == 250
    assert playground_obj.y_max == 250
    assert len(playground_obj.holes) == 0
    assert playground_obj.shape == Polygon([(-250, -250), (-250, 250), (250, 250), (250, -250)])

def test_func_position_is_in_playground():
    """Test method is_position_in_playground for Point in Playground"""
    test_position = (0.5, 0.5)
    playground = Playground(x_max=1, y_max=1)
    assert playground.is_position_in_playground(test_position[0], test_position[1]) is True

def test_func_position_is_not_in_playground():
    """Test method is_position_in_playground for Point outside Playground"""
    test_position = (1.5, 1.5)
    playground = Playground(x_max=1, y_max=1)
    assert playground.is_position_in_playground(test_position[0], test_position[1]) is False