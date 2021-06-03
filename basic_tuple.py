def define_tuple():
    tp = tuple()
    print(tp, type(tp))

    # casting
    tp = tuple({1, 3, 5, 7, 9})
    print(tp, type(tp))

    tp = ()
    tp2 = (1,)  # must include    ,     at the end
    tp3 = (1, 2, 3)
    print(tp, tp2, tp3)


def tuple_oper():
    tp = (1, 2, 3, 4, 5)
    print(tp, len(tp))
    print(tp[0], tp[1], tp[2], tp[3], tp[4])
    print(tp[-5], tp[-4], tp[-3], tp[-2], tp[-1])

    # tp[3] = 0     tuple = immutable, change(x)

    # list, repetition, in, not in = BASIC_LIST


def tuple_method():
    tp = (20, 30, 10, 20)
    print(tp.index(20))
    print(tp.index(20, 1))  # defining the search range from index point
    print(tp.count(20))


def packing_unpacking():
    tp = (10, 20, 30, "Python")
    print(tp, type(tp))
    tp = 10, 20, 30, "Python"  # without () : still tuple  = packing
    print(tp, type(tp))

    (a, b, c, d) = tp
    print(tp)
    print(a)
    print(a, b, c, d)

    # a, b, c, = tp     # 3 != 4 ERROR
    # a, b, c, d, e = tp  # 5 != 4 ERROR

    '''Python 3 * vs Python 2 [:]
    a, *b = tp
    a, b = tp[0:1]         # a = 10, b = 20, 30, Pythong
    print(a, b)

    *a, b = tp 
    print(a, b)
    a, *b, c = tp
    print(a, b, c)
    '''


if __name__ == "__main__":
    # define_tuple()
    # tuple_oper()
    # tuple_method()
    packing_unpacking()