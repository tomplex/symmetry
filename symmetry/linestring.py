from symmetry import Point
from symmetry.exc import ArgumentError


class LineString:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], Point) or len(args[0]) <= 1:
                raise ArgumentError("Lines must consist of 1 or more Points.")

            self.__coords = list(args[0])
        elif len(args) > 1:
            self.__coords = list(args)
        else:
            self.__coords = []

    def __len__(self):
        return len(self.__coords)

    def __getitem__(self, item):
        return self.__coords[item]

    def __eq__(self, other):
        if not isinstance(other, LineString):
            return False
        return all([other[i] == pt for i, pt in enumerate(self)])

    @property
    def coords(self):
        return list(self.__coords)

