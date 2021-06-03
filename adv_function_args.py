def sum_val(a, b):
    return a + b

def incr(a, step=1):    # 1 = set value
    return a + step

print(sum_val(2, 3))
print(incr(10))         # if not specify, 2nd value -> 1
print(incr(10, 2))      # specified -> 2nd set value : ignored

# keyword
# the order does not matter
def area(width, height):
    print "width : ", width
    print "height : ", height
    return width * height

print(area(10, 20))
print(area(height=12, width=10))

# *
def get_total(*args):
    total = 0
    print(args, type(args))
    for x in args:
        total += x
    return total

print(get_total(1, 3, 5, 7, 9))




def get_total2(*args):
    total = 0
    for x in args:
        if isinstance(x, (int, float)):
            total += x
        elif isinstance(x, (list, tuple)):
            for item in x:
                if isinstance(item, (int, float)):
                    total += item

    return total

print(get_total2(1, 2, 3, 4, 5))
print(get_total2(1, 2, "3", 4, 5))
print(get_total2(1, 2, [3, 4, 5]))




def args_test(a, b, *args, **kwd):
    # a, b : set value
    # args : not set
    # keyword
    print(a, b)
    print(args)
    print(kwd)

# the order**
args_test(10, 20, 30, 40, 50, option1="value1", option2="value2")

def plus(a, b):
    return a + b
def minus(a, b):
    return a - b

def calculator(a, b, func):
    if (callable(func)): # to check if func is function
        return func(a, b)

print(calculator(1, 2, plus))



dirty_strings = "python pRogRamming, jaVa pRogRaMMing, LiNUx".split(",")
print(dirty_strings)

def clean_string(strings, *funcs):
    results = []
    for string in strings:
        for func in funcs:
            if callable(func):
                string = func(string)
        results.append(string)
    return results

# *funcs => str.strip, str.title
cleaned = clean_string(dirty_strings, str.strip, str.title)
print("Cleaned : ", cleaned)

# __name__
# if imported --> the name itself

# if executed by itself  -> __main__
print("__name__", __name__)

if __name__ == "__main__":
    print("the highest module executed")
else:
    print("imported")