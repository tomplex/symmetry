from symmetry.exc import ArgumentError


class Point:

    def __init__(self, *args):
        if len(args) > 2:
            raise ArgumentError("Point must be called with x,y or [x, y] arguments")
        elif len(args) == 0:
            self.__x, self.__y = None, None
        elif len(args) > 1:
            # x, y constructor
            self.__x, self.__y = args[0], args[1]
        else:
            # [x,y] constructor
            self.__x, self.__y = args[0]

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def bounds(self):
        """
        Bounds of the geometry in (xmin, ymin, xmax, ymax)

        """
        return (
            self.x, self.y,
            self.x, self.y
        )
