def square(x):
    return x ** 2

for i in range(10):
    print("{}:{}".format(i, square(i))),
else:
    print ""

for i in range(10):
    print("{}:{}".format(i, (lambda x: x ** 2)(i))),
else:
    print ""

# using lambda - sort function
strings = "Life is too short. Get a cat".upper().replace(",","").split()
print("STRINGS : ", strings)

def strlen(x):
    return len(x)

result = sorted(strings, key=lambda x: len(x), reverse=True)
print("LEN DESC : ", result)
