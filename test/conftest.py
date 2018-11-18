import pytest

from symmetry import Point
from test.helpers import get_origin_to_one_linestring, get_origin_point, get_origin_plus_one_point


@pytest.fixture()
def origin_point():
    return get_origin_point()


@pytest.fixture()
def plus_1_point():
    return get_origin_plus_one_point()


@pytest.fixture()
def origin_to_one_linestring():
    return get_origin_to_one_linestring()
