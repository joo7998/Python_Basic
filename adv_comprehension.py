def list_comprehension():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = []

    # FOR
    for num in nums:
        result = num * num
        results.append(result)
    print(results)

    # List Comprehension
    results = [num * num for num in nums]
    print(results)

    results = []
    strings = ['a', 'as', 'bat', 'car']

    # FOR
    for item in strings:
        if len(item) <= 3:
            results.append(item)
    print(results)

    # List Comprehension
    results = [item for item in strings if len(item) <= 3]
    print(results)

    # even num list
    evens = [i for i in range(1, 101) if i % 2 == 0]
    print(evens)




def set_comprehension():
    # Syntax : { expression for     variable   in  range    if    condition }
    # set = no order, no repetition
    strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
    results = {item for item in strings if len(item) <= 3}
    print(results)

    results = {len(item) for item in strings}
    print(results)      # no repetition for 3

def dict_comprehnsion():
    strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
    dct = {item:len(item) for item in strings}
    print(dct)





if __name__ == "__main__":
    # list_comprehension()
    # set_comprehension()
    dict_comprehnsion()