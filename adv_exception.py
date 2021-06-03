def handling_exception():
    lst = []

    try:
        lst[3] = 1
        4 / 0
        int("String")
    except Exception:
        print("Error")

    try:
        # lst[3] = 1
        # 4 / 0
        int("String")
        print(int(12345))
    except ValueError as e:
        print("Can not change to int")
        print(e, type(e))
    except ZeroDivisionError as e:
        print("You can not divide with 0")
        print(e, type(e))
    except IndexError as e:
        print("Can not access index")
        print(e, type(e))
    except Exception as e:
        print("Error")
        print(e, type(e))

    else:
        print("No exception")
    finally:
        print("the end of exception handling")

    # exception (o) : try -> except -> finally
    # exception (X) : try -> else -> finally

def raise_exception():

    def beware_dog(animal):
        if animal == "dog":
            raise RuntimeError("No dogs allowed")
        else:
            print(animal, "Welcome")

    try:
        beware_dog("cat")
        beware_dog("cow")
        beware_dog("dog")
    except Exception as e:
        print(e, type(e))

    print("End of code")


if __name__ =="__main__":
    # handling_exception()
    raise_exception()
