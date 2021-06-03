numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
evens = {0, 2, 4, 6, 8}
odds = {1, 3, 5, 7, 9}
mthree = {0, 3, 6, 9}

def define_set():
    empty = set()
    print(empty, type(empty))
    empty = {}                  # dict
    print(empty, type(empty))

    print(numbers, len(numbers))
    print(2 in numbers, 2 in evens, 2 in odds)

    s = "Python Programming"
    chars = set(s.upper())
    print(s, chars)

    lst = "Python Programming in Java Programming".upper().split()
    print(lst)

    words = set(lst)
    print(words, len(words))

def set_methods():
    print (numbers)
    numbers.add(10)
    print(numbers)
    evens.add(10)
    print(evens)

    evens.add(4)        # set : repetition (x)
    print(evens)

    evens.discard(4)
    print(evens)
    evens.discard(4)    # set : repetition (x)
    print(evens)

    evens.update({2, 4, 6})
    print(evens)

def set_oper():
    print(evens.union(odds))
    print(evens | odds)

    print(numbers.issuperset(evens))
    print(odds.issubset(numbers))

    print(evens.intersection(mthree))
    print(mthree & odds)

    print(numbers.difference(evens))
    print(numbers - evens)


def loop():
    for item in numbers:
        print(item),
    else:
        print()


if __name__ == "__main__":
    # define_set()
    # set_methods()
    # set_oper()
    loop()