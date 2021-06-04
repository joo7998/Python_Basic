def list_comprehension():
    """
    Syntax: [ -- for -- in -- if condition ]
    """

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = []

    for num in nums:
        result = num * num
        results.append(result)
    print("Result:", results)

    results = [ num * num for num in nums]
    print("Result:", results)

    strings = ['a', 'as', 'bat', 'car', 'dove', 'python']

    results = []
    for item in strings:
        if len(item) <= 3:
            results.append(item)
    print("FOR Result:", results)

    results = [item for item in strings if len(item) <= 3]
    print("Result:", results)

    evens = [i for i in range(1, 101) if i % 2 == 0]
    print("Evens:", evens)


def set_comprehension():
    strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
    results = {item for item in strings if len(item) <= 3}
    print(results)

    results = {len(item) for item in strings}
    print(results)


def dict_comprehension():
    strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
    dct = {item:len(item) for item in strings}
    print(dct)


if __name__ == "__main__":
    # list_comprehension()
    # set_comprehension()
    dict_comprehension()