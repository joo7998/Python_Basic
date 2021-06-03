def q1():
    s = "Life is too short, You need Python"

    s = s.lower()\
            .replace(",", "")\
            .replace(" ", "")

    # list
    lst = list(s)
    # to set (no repeat)
    chars = set(lst)
    print("chars:", chars)
    # to list
    lst = list(chars)
    lst.sort()
    print(lst)
    print(len(lst))


def q2():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    slice = lst[3:7]
    slice.reverse()
    lst[3:7] = slice

    print(lst)
    print(lst == [1, 2, 3, 7, 6, 5, 4, 8, 9, 10])


def q3():
    students = [
        {
            "name": "Kim",
            "kor": 80,
            "eng": 90,
            "math": 80
        },
        {
            "name": "Lee",
            "kor": 90,
            "eng": 85,
            "math": 85
        }
    ]

    for student in students:
        total = student.get("kor") + \
                student.get("eng") + \
                student.get("math")
        average = total / 2
        student['total'] = total
        student['average'] = average

    print(students)


if __name__ == "__main__":
    q1()
    q2()
    q3()