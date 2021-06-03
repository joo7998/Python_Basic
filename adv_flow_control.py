def if_statement():

    money = int(input("how much do you have?"))

    message = ""
    if money >= 10000:
        message = "by taxi"
    elif money >= 1000:
        message = "by bus"
    else:
        message = "on foot"

    print(message)

def cond_expr():
    money = int(input("how much do you have?"))
    message = "by taxi" if money >= 10000 else "by bus" if money >= 1000 else "on foot"
    print(message)



def for_ex():
    # for in
    a = ["cat", "coco", "dog"]
    for animal in a:
        print (animal),
    else:
        print""

    for index, color in enumerate(['red', 'blue', 'green']):
        print(index, color)

    total = 0
    for i in range(1, 11):
        total += i

    print(total)

    # break
    r1 = list(range(1, 12, 2)) + [12, 13, 15]
    print(r1)

    for i in r1:
        if i % 2 == 0:
            print "found the even number: ", i
            break
    else:
        print("No even number")

    # continue
    for i in range(11):
        if i % 2 == 0:
            continue
        print(i),
    else:
        print ""

# example 1 (multiplication)
for i in range(2, 10):
    for j in range(1, 10):
        print i, "X", j, "=", i * j
        if (j == 9):
            print""

# example 2 (draw a triangle)
for n in range(1, 5):
    print('*'*n)





if __name__ == "__main__":
    # if_statement()
    # cond_expr()
    for_ex()
