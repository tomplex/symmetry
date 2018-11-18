import pytest

from symmetry import LineString, Point
from symmetry.exc import ArgumentError
from test.helpers import get_origin_to_one_linestring, get_origin_plus_one_point, get_origin_point


def test_create_linestring_list_of_points():
    l = LineString([Point(0.0, 0.0), Point(1.0, 1.0)])
    print(l.coords)
    assert len(l) == 2


def test_create_linestring_from_pt_args():
    l = LineString(Point(0.0, 0.0), Point(1.0, 1.0), Point(2.0, 2.0))
    assert len(l) == 3


def test_create_linestring_with_one_point():
    with pytest.raises(ArgumentError):
        l = LineString([Point(0.0, 0.0)])


def test_create_linestring_with_one_point_arg():
    with pytest.raises(ArgumentError):
        l = LineString(Point(0.0, 0.0))


def test_create_empty_linestring():
    l = LineString()
    assert len(l) == 0


def test_user_cant_change_linestring_coords():
    l = LineString(Point(0.0, 0.0), Point(1.0, 1.0))

    coords = l.coords
    coords[0] = Point(1.0, 2.0)

    assert l.coords[0] == Point(0.0, 0.0)


def test_linestring_equality():
    l1 = get_origin_to_one_linestring()
    l2 = get_origin_to_one_linestring()

    assert l1 == l2


def test_linestring_not_equal():
    # Also shows that ordering matters
    l1 = get_origin_to_one_linestring()
    l2 = LineString(get_origin_plus_one_point(), get_origin_point())

    assert l1 != l2

