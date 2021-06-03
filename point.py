class Point:
    instance_count = 0

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    #  __init__
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        Point.instance_count += 1

    #  __del__
    def __del__(self):
        Point.instance_count -= 1

    #
    def __str__(self):
        return "Point x={}, y={}".format(self.x, self.y)

    #
    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    #
    def __add__(self, other):
        # Point + other
        if isinstance(other, Point):  # + Point
            return Point(self.x + other.x,
                         self.y + other.y)
        elif isinstance(other, int):  # + int
            return Point(self.x + other,
                         self.y + other)

        return self + other

    #
    def __radd__(self, other):  # other + Point
        if isinstance(other, int):
            return Point(self.x + other,
                         self.y + other)

        return other + self

    #
    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x,
                         self.y - other.y)
        elif isinstance(other, int):
            return Point(self.x - other,
                         self.y - other)

        return self - other

    # == overloading
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y