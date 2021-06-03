def using_range():
    seq = range(10)
    print(seq, type(seq))
    print(list(seq))

    seq2 = range(2, 10)
    print(seq2)
    print(list(seq2))

    seq3= range(2, 10, 2)
    print(seq3)
    print(list(seq3))

    seq4= range(0, -10, -1)
    print(seq4)
    print(list(seq4))

    print(seq, len(seq))

    print(5 in seq)

    print(seq[0], seq[1], seq[2])
    print(seq[-1], seq[-2], seq[-3])

    print(seq[2:5])
'''
    for i in range(10):
        print(i, end=" ")
    else:
        print()
'''

def using_enumerate():
    colors = ["red", "yellow", "blue"]

    i = 0
    for color in colors:
        print("COLOR {0}: {1}".format(i, color))
        i += 1

    print("ENUMERATE")
    for index, color in enumerate(colors):
        print("COLOR {}: {}".format(index, color))

def using_zip():
    # zip
    english = "Sun", "Mon", "Tue", "Wed"
    korean = "IL", "WOL", "HWAW", "SU", "MOK"
    engkor = zip(english, korean)

    print(engkor, type(engkor))


    for pair in engkor:
        print(pair, type(pair))


    engkor = zip(english, korean)

    # unpacking loop
    for eng, kor in engkor:     # tuple -> unpacking
        print(eng, "->", kor)

    engkor = zip(english, korean)
    # index, en, kr
    for index, (eng, kor) in enumerate(engkor):
        print(index, eng, kor)

    # zip -> dict
    print(dict(zip(english, korean)))


if __name__ =="__main__":
    # using_range()
    # using_enumerate()
    using_zip()