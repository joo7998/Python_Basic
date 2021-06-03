x = 1
def scope_func(a):
    return a + x        # local scope : no x -> global scope search

def scope_func2(a):
    x = 2               # local scope x (created) != global x
    return a + x        # local scope a , local scope x

print(scope_func(10))
print(scope_func2(10))
print "global x : ", x      # scope_func2 x changed , not global x


g = 1       # gloabl
def scope_func3(a):
    global g
    g = 3
    return a + g

print(scope_func3(10))
print "global g : ", g

print(dir())
print(dir('__builtins__'))