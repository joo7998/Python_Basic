def define_str():
    s0 = 'Hello Python'
    s1 = "Hello Python"
    s2 = str("Hello Python")
    s3 = str(3.14159)

    print(s1, s2, s3)
    print(type(s1), type(s2), type(s3))

    print(isinstance(s1, str))

    s4 = """Life is too short. You need python. 
Python is useful for data analysis. 



"""
    print(s4)


def string_oper():
    """
         str: len
             +(connect) *(repeat)
             indexing, slicing
             immutable (no change)
    """
    str1 = "Python"
    str2 = "Second String"
    print(len(str1))

    # str : no chagne
    # str1[0] = 'f'

    # indexing
    print str1[0], str1[1], str1[2], str1[3], str1[4], str1[5]
    print str1[-6], str1[-5], str1[-4], str1[-3], str1[-2], str1[-1]

    # slicing
    print(str1[2:4])
    print(str1[-4:-2])
    print(str1[0:3])
    print(str1[:3])
    print str1[3:len(str1)]
    print str1[3:]
    print(str1[:])
    print(str1[::2])
    print(str1[::-1])  # if the gap is (-): the opposite order

    # + (connection, NOT PLUS)
    print(str1 + " Programming")

    # * (repetition)
    print(str1 * 3)

    # in / not in
    print("P" in str1)
    print("P" not in str1)


def transform_methods():
    s = "i like python"
    print(s)
    print(s.upper())
    print(s.lower())
    print(s.swapcase())
    print(s.capitalize())  # only the first letter of the sentence
    print(s.title())  # each first letter : capital

    print(s)  # str = immutable = the original str stays the same


def search_method():
    s = "I Like Python. I Like Java Also"
    print(s)
    print(s.count("Like"))

    print(s.find("Like"))  # index
    print(s.find("Like", 6))  # after 6th index
    print(s.find("Like", 20))  # none = -1

    print(s.index("Like"))
    print(s.index("Like", 6))
    # print(s.index("Like", 21))  # none = ERROR

    if "Like" in s[21:]: print(s.index("Like", 21))

    print(s)
    # opposite direction
    print(s.rfind("Like"))
    print(s.rfind("Like", 0, 17))

    url = "http://www.naver.com"
    surl = "https://www.naver.com"
    ftp = "ftp://ftp.naver.com"

    print(url.startswith("http://"))
    print(surl.startswith("https://"))
    print(ftp.startswith(("http://", "https://")))
    print(url.startswith(("http://", "https://")))
    print(url.endswith("naver.com"))

    print(ftp.startswith("ftp.", 6, 20))


def modify_replace_method():
    s = "        Alice and the Heart Queen      "
    print s.strip()
    print s.lstrip()
    print s.rstrip()

    s = "----------Alice and the Heart Queen-----"
    print(s.strip("-"))

    s = "I Love Java"
    print(s)
    print(s.replace("Java", "Python"))
    print(s)


def split_join_methods():
    s = "Ham and Cheese and Bread and Ketchup"
    print(s)
    print(s.split())
    items = s.split(" and ")
    print(items)

    items = s.split(" and ", 2)
    print(items)

    items = s.rsplit(" and ", 2)
    print(items)

    lines = """
Java Programming 
Python Programming
Oracle Database
    """

    print(lines.split())  # tab, space, new line
    print(lines.splitlines())  # line
    print(lines.splitlines(True))  # not deleting \n


def check_method():
    print("1234567890".isdigit())
    print("abcdefg".isalpha())
    print("Python3".isalnum())
    print("Python 3".isalnum())  # space
    print(" \r\n\t".isspace())
    print("".isspace())

    print("PYTHON".isupper())
    print("python".islower())
    print("Python Programming".istitle())


def align_method():
    s = "Alice and the Heart Queen"
    print(s.center(60))
    print(s.center(60, "*"))
    print(s.ljust(60, "*"))
    print(s.rjust(60, "*"))
    # zero fill
    print("1234".zfill(5))
    print("1234567890".zfill(5))


# %s(str) %c %d(decimal) %f(floating) %o %x %%(% itself)
def string_format():
    fmt = "My name is %s and my age is %d!"
    print fmt % ('Bob', 30)
    print ("Current interest rate is %.2f%%" % 1.2345)

    # named formatting
    fmt = "%(total)d %(fruit)s I ate %(eat)d"
    # print fmt %("total": 3)

    # format method
    fmt = "Out of {} {} , ate {}"
    print(fmt.format(10, "apples", 2))

    fmt = "Out of {0} {1}, ate {2}"
    print(fmt.format(3, "peaches", 1))

    fmt = "Out of {total} {fruit}, had {eat}"
    print(fmt.format(eat=3, fruit="melons", total=4))

    # named parameter : .format_map
    # print("Out of {total} {fruit}, had {eat}".format_map({
    #    "total": 7 "fruit": "orange" "eat": 2
    # }))

    # f F
    total, fruit, eat = 10, 'apple', 1
    # print(f"{total} {fruit.upper()} ate {}. Left with {total - eat}")


if __name__ == "__main__":
    # define_str()
    # string_oper()
    # transform_methods()
    # search_method()
    # modify_replace_method()
    # split_join_methods()
    # check_method()
    # align_method()
    string_format()