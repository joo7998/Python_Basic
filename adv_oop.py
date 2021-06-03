class MyString(str):        # MyString inherited str class
    pass                    # MyString inherits all the members from str class

s = MyString()              # instance created
print(type(s))
print(MyString.__bases__)   # base class ?
print(str.__bases__)        # object = the highest class of all the classes

class myobj:
    pass

class Chimera(str, myobj):
    pass

print(type(Chimera))
print(Chimera.__bases__)

#issubclass
print(issubclass(Chimera, str))
print(issubclass(Chimera, myobj))

# MyString inherited str -> MyString inherited str's member
ms = MyString("Python")
print(ms)
print(dir(ms))
print(ms.upper())

# Class
