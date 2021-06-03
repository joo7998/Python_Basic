def define_dict():
    dct = dict()
    print(dct, type(dct))
    dct = {"basketball": 5, "baseball": 9}

    dct['volleyball'] = 6
    print(dct)
    print(len(dct))
    print("scoccer" in dct)
    print("baseball" in dct)

    print(dct.keys(), type(dct.keys()))
    print(dct.values(), type(dct.values()))
    print(dct.items(), type(dct.items()))

    print(9 in dct.values())

    d1 = dict(key1="value1", key2="value2")
    print(d1, type(d1))

    d2 = dict([('key1', 'value1'), ('key2', 'value2')])
    print(d2, type(d2))

    keys = ('one', 'two', 'three')
    values = (1, 2, 3, 4)
    d3 = dict(zip(keys, values))
    print(d3, type(d3))

    # set key = non changeable
    d4 = {}
    d4[True] = "true"
    d4[10] = 10
    d4['eleven'] = 11
    d4[(10, 'hong')] = 100

    #d4[[1, 2, 3]] = 100

def dict_methods():
    dct = {"soccer": 5, "baseball": 9, "volleyball": 6}
    print(dct)

    keys = dct.keys()
    print(type(keys))

    lst_keys = list(keys)       # dict_keys -> list
    print(lst_keys, type(lst_keys))

    values = dct.values()
    print(values, type(values))

    # (key, value) double tuple : items()
    items = dct.items()
    print(items, type(items))
    lst_items = list(items)
    print(lst_items, type(lst_items))

    # tuple list -> access by index
    print(lst_items[0][0], lst_items[0][1])

    dct.clear()
    print(dct)

def using_dict():
    phones = {
        "a": "010-1234-5678",
        "b": "010-9876-5432"
    }
    print(phones)

    # add
    phones['c'] = '010-5432-2109'
    print(phones)

    print('a', phones['a'])
    # print('c', phone['c'])        # KeyError (n/a)
    print('c', phones.get('c'))

    # get() method :
    #   1. no key, not having to get error -> get the none value
    #   2. key (o) -> dont want none value
    print("d", phones.get('d', 'no phone num'))

    # delete
    del phones['b']
    print(phones)

    # pop
    print(phones.pop('a'))
    print(phones)


def loop():
    phones = {
        "a": "010-1234-5678",
        "b": "010-9876-5432"
    }
    print(phones)

    for key in phones:
        print(key + ": " + phones.get(key))
    print()

    for key in phones.keys():
        print(key + ": " + phones.get(key))
    print()

    # unpacking
    for key, value in phones.items():
        print(key + ": " + phones.get(key))



if __name__ == "__main__":
    # define_dict()
    # dict_methods()
    # using_dict()
    loop()