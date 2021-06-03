def define_list():

    lst1 = list()
    print(lst1, type(lst1))
    lst2 = []
    lst3 = [1, 2, "python"]
    print (lst2, lst3)
    lst4 = list("Python")
    print(lst4)  # squence -> list

def list_oper():
    lst = [1, 2, "Python"]
    print(lst, len(lst))
    print(lst[0], lst[1], lst[2])
    print(lst[-3], lst[-2], lst[-1])
    print(lst[1:3])
    print(lst[1:])
    print(lst[:3])

    copy = lst[:]
    print(copy)
    print(copy is lst)

    # + : data change (x)
    # extend : data change (o)
    print(lst + ["Java", True, 3.14])
    print(lst)

    # append vs extend
    copy.append(["Java", True, 3.14159])  # the whole lot
    print(copy)
    copy.extend(["Java", True, 3.14])     # as an individual list
    print(copy)

    # insert
    copy.insert(2, [1, 2, 3])   # insert (index n, to add)
    print(copy)

    # * repetition
    print(lst)
    print(lst * 3)

    # in , not in
    print("Python" in lst)

    # index check
    print(lst.index("Python"))
    #print(lst.index("Java"))  # IF NOT there : ERROR
    if "Java" in lst:
         print("INDEX:", lst.index("Java"))
    print(copy)

    print(copy.count("Python"))

    # delete
    del copy[0]
    print(copy)

    # remove
    copy.remove(3.14)
    print(copy)

    # slicing -> change
    lst = [1, 12, 123, 1234, 12345]
    print(lst)
    lst[0:2] = [10, 20]  # index 0~2 : change with [10, 20]
    print(lst)

    #slicing -> delete
    lst[0:2] = []       # index 0~2 : delete
    print(lst)

    # slicing -> insert
    lst[1:1] = ['inserted']
    print(lst)

    # slicing -> append
    lst[4:] = ['appended']
    print(lst)

    # prepend
    list[:0] = ["prepended"]
    print(lst)

    lst = [1, 2, 3]
    print(sum(lst))
    print(min(lst))
    print(max(lst))
    print(sum(lst)/len(lst))

def list_method():

    lst = [1, 2, 9]
    print(lst)
    copy = lst.copy()

    # Reserve ??? doesnt work
    copy.reverse()
    print(copy)

    copy = lst.copy()
    print(copy)

    result = sorted(copy)
    print(result)
    result = sorted(copy, reverse=True)
    print(result)

    print(copy)
    result = sorted(copy, key=str)
    print(result)

    def key_func(val):
        return val % 5
    result = sorted(copy, key=key.func, reverse=True)

    print(sorted(result))

    copy.sort(key=key_func, reverse=True)
    print(copy)

def stack_ex():
    stack = []
    stack.append(10)
    stack.append(20)
    stack.append(30)
    print(stack)

    print(stack.pop())      # from the rear
    print(stack.pop())
    print(stack.pop())
    if len(stack):
        print(stack.pop())    # ERROR
    else:
        print("The stack is empty")

def queue_ex():     # append, pop
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    print(queue)

    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))

def loop():
    words = "Life sucks. You need to chill".replace(",", "").upper().split()
    print(words)

    for word in words:
        print(word)


if __name__ =="__main__":
    # define_list()
    # list_oper()
    # list_method()
    # stack_ex()
    # queue_ex()
    loop()
