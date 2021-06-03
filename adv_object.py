# global variable

global_a = 1
global_b = "GLOBAL SCOPE"

# function

def func():
    # local variable
    local_a = 2
    local_b = "LOCAL SCOPE"
    # local symbol table check
    print(locals())

class MyClass:
        x = 10
        y = 20

# symbol table check
def symbol_table():
    # global symbol table check
    print(globals())
    print(type(globals()))

    # symbol table [dict - variable symbol & variable id]
    print(globals().get("global_a"))
    print(globals().get("global_b"))

    func()

    # inside __dict__ -> inside symbol table
    # 1. defined symbol table
    func.dynamic = "Hello"
    print(func.__dict__)
    # 2. inside class --> inside symbol table
    print(MyClass.__dict__)
    print(int.__dict__)

def ref_count():
    x = object()
    print(x, type(x))

    import sys      # system module import
    print(sys.getrefcount(x))

    y = x           # +1 ref count
    print(sys.getrefcount(x))

    # delete x ref
    del x
    print(sys.getrefcount(y))

    # if ref count = 0 -> G.C

# id = ref address
def object_id():
    # same
    i1 = 10
    i2 = int(10)
    print(hex(id(i1)), hex(id(i2)))

    # not same
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    print(hex(id(lst1)), hex(id(lst2)))

    # copy = same
    lst3 = lst2
    print(hex(id(lst2)), hex(id(lst3)))

    # == : equal value, is : same variable
    print(i1 == i2, i1 is i2)               # same value, same variable
    print(lst1 == lst2, lst1 is lst2)       # same value, not same variable

def object_copy():
    import copy

    # ref copy = only copy the address
    a = 1
    b = a
    print(a is b)

    # shallow copy
    a = [1, 2, 3]
    b = [4, 5, 6]
    x = [a, b, 100]
    print(a)
    print(b)
    print(x)

    y = x
    print(x is y)  # same variable
    x[0][2] = 10   # 0th index's 2th index
    print(x)
    print(y)

    y = copy.copy(x)
    print(x is y)   # different variable
    print(x)
    print(y)
    x[0][2] = 3
    print(x)
    print(y)

    print('x[0] is y[0]?: ', x[0] is y[0])

    # deep copy
    y = copy.deepcopy(x)
    print(x is y)
    print(x[0] is y[0])
    print(x[1] is y[1])

    x[0][2] = 20
    print(x)
    print(y)


if __name__ == "__main__":
    # symbol_table()
    # ref_count()
    # object_id()
    object_copy()
