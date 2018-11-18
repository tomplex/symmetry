import pytest

from symmetry import Point
from symmetry.exc import ArgumentError


def test_create_point(origin_point):
    assert isinstance(origin_point, Point)


def test_x_property(origin_point):
    assert origin_point.x == 0.0


def test_y_property(origin_point):
    assert origin_point.y == 0.0


def test_bounds(origin_point):
    assert origin_point.bounds == (0.0, 0.0, 0.0, 0.0)


def test_invalid_constructor_extra_arg():
    with pytest.raises(ArgumentError) as exc:
        p = Point(0.0, 0.0, 0.0)


def test_empty():
    p = Point()
    assert p.x == None
    assert p.y == None


def test_equals():
    p1 = Point(0.0, 0.0)
    p2 = Point(0.0, 0.0)

    assert p1 == p2

