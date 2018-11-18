from symmetry import LineString, Point


def get_origin_to_one_linestring():
    return LineString(Point(0.0, 0.0), Point(1.0, 1.0))


def get_origin_point():
    return Point(0.0, 0.0)


def get_origin_plus_one_point():
    return Point(1.0, 1.0)
