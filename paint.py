# Test
from point import Point

def bound_class_method():
    # specify instance -> access member
    p = Point()
    p.setX(10)
    p.setY(20)
    print(p.getX(), p.getY()),
    print(p.getX, p.getY)
    # getX, getY <-- bound method


def unbound_class_method():
    p = Point()
    Point.setX(p, 10)
    Point.setY(p, 20)
    print(Point.getX(p), Point.getY(p))
    print(Point.getX, Point.getY)
    # Point class function


def class_member_test():
    p1 = Point()
    p1.setX(10)
    p1.setY(20)

    print("p1: {}, {}".format(p1.getX(), p1.getY()))
    print("instance_count:",
          p1.instance_count,    # access from instance
          Point.instance_count) # access without instance


def test_lifecycle():
    p1 = Point(10, 20)
    print("instance count:", Point.instance_count)

    p2 = Point()
    print("instance count:", Point.instance_count)

    print(p1, p2)


def test_print():
    p1 = Point(10, 10)
    print("p1:", p1)    # __str__

    # __str__ : for users to see easily
    # __repr__: for developer to restore the object

    print(repr(p1)) # __repr__
    p2 = eval(repr(p1)) # __repr__ --> restore the object
    print("p2:", p2, type(p2))

    # __str__ : unofficial (normal user)
    # __repr__ : official (developer)


def arith_oper_overriding():
    p1 = Point(10, 20)
    p2 = Point(30, 40)

    # print(dir(object))
    # Point + Point
    print(p1 + p2)

    # Point + int
    p1 = Point(10, 20)
    print(p1 + 10)

    # int + Point
    p1 = Point(10, 20)
    print("int + Point:", 10 + p1)

    # ex
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(p1 - p2)

    p1 = Point(10, 20)
    print(p1 - 10)

    p1 = Point(10, 20)
    p2 = Point(10, 20)

    print("p1 == p2?", p1 == p2)

if __name__ == "__main__":
    # bound_class_method()
    # unbound_class_method()
    # class_member_test()
    # test_lifecycle()
    # test_print()
    arith_oper_overriding()