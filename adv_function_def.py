def dummy():
    pass

def my_function():
    print("Hello Python")

def times(a, b):
    return a * b

def none():
    return          # full stop the function

dummy()
print(dummy())
print(times(10, 2))
print(none())
print(none())



# function = also a variable ( id, address )
fun = times   # referring def time(a, b) -> return a  * b
print(fun(10, 20), type(fun))

# isinstance (x) , callable
print "fun is callable? : ", callable(fun)

if callable(fun):
    print(fun(10,4))

# return ( 1 result)
def max_value(a, b):
    if a > b:
        return a
    else: return b

print(max_value(10, 20))

# return ( +2 result)
def swap(a, b):
    return b, a     # packing in tuple

print(swap(10, 20), type(swap(10, 20)))

# unpacking
c, d = swap(10, 20)
print(c, d)
