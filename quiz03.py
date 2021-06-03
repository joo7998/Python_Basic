def q1():
    while True:
        num = input("enter a num:")

        try:
            int(num) # casting
        except:
            print("enter integer")
        else: # not in try block
            break

    total = 0
    to = int(num)

    # for i in range(1, to + 1):  # 1 ~ to
    #     if i % 3 == 0:
    #         total += i
    lst = [i for i in range(1, to + 1) if i % 3 == 0]   # 3X list
    total = sum(lst)

    print("1 ~ {} 3X sum = {}".format(to, total))


def q2():
    lst = [1, 3.14, 'python', 7, 89.1, 3]
    # lst_cleaned = []
    # for item in lst:
    #     if isinstance(item, (int, float)):
    #         lst_cleaned.append(item)
    lst_cleaned = [item for item in lst if isinstance(item, (int, float))]
    print("cleaned:", lst_cleaned)


def summary(*args):
    total = sum(args)
    return total, max(args), min(args), total / len(args)


def q3():
    total, maxval, minval, avg = summary(80, 75, 90, 95, 85)
    print(total, maxval, minval, avg)


def q4():
    s = """We encourage everyone to contribute to Python. 
    If you still have questions after reviewing the material
    in this guide, then the Python Mentors 
    group is available to help guide new contributors through the process."""


    s = s.replace(",", "").replace(".", "").replace("\n", "").upper()
    splits = s.split()
    print("splits:", splits)

    summary = {}    # result dict
    for word in splits:
        if word in summary.keys():  # if key already
            summary[word] += 1
        else:   # if no key
            summary[word] = 1

    for key, value in summary.items():  # (key, value) tuple
        print("{}: {}".format(key, value))

if __name__ == "__main__":
    # q1()
    # q2()
    # q3()
    q4()