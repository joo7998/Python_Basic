def q1():
    score1 = int(input("Score 1:"))
    score2 = int(input("Score 2:"))

    average = (score1 + score2) / 2

    if score1 >= 50 and \
        score2 >= 50 and \
        average >= 60:
        message = "PASS"
    else:
        message = "FAIL"

    print(message)


def q2():
    for dan in range(2, 10):
        print(dan, "DAN")
        for num in range(1, 10):    # 1 ~ 9
            print("{} x {} = {}".format(dan, num, dan * num))


def q3():
    balance = 0

    while True: # loop infinite
        method = input("method:")
        method = method.lower()

        if method == "q":
            break   # end of the loop

        if method != "d" and method != "w":
            print("?")
            continue


        amount = int(input("Amount:"))

        # if method == "d":
        #     balance += amount
        # else:
        #     balance -= amount
        balance += amount if method == "d" else -amount

        print("Balance:", balance)

    print("the end")


if __name__ == "__main__":
    # q1()
    # q2()
    q3()
