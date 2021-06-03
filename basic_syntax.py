def arith_oper():

    # +, -, *, /
    print(7/3)
    print(6/2)

    print(7//3)
    print(7 % 3)

    print(divmod(7, 3))
    print(divmod(7, 3)[0])
    print(divmod(7, 3)[1])

    print(7**3)
    print(pow(7, 3))

def complex_ex():
    print(3+4j)
    print(3+4j.real)
    print(3+4J.imag)
    print(3+4J.conjugate())

    print(complex(3, 4))

def rel_oper():
    print("1 > 3 ?", 1 > 3)
    print("1 < 3 ?", 1 < 3)
    print("6 equals 9 ?", 6 == 9)
    print("6 not equals 9 ?", 6 != 9)

    s1 = "Python"
    s2 = "Python"

    print(s1 == s2)

    a = 6

    print(a > 0 and a < 10) #
    print(0 < a and a < 10) #
    print(0 < a < 10)   #

    print("abcd" > "abd")
    print((1, 2, 4) > (1, 3, 1))
    print([1, 2, 4] < [1, 3, 1])

    a = 10
    b = 20
    c = a
    print("a == b ?", a == b)
    print("a is b ?", a is b)
    print("a == c ?", a == c)
    print("a is c ?", a is c)

def variable_ex():
    import keyword
    print(keyword.kwlist)
    print(len(keyword.kwlist))

    price = 12000
    print(price + price * 0.1)

def assginment_ex():

    a, b = 3.5, 5.3
    print(a, b)

    a, b = b, a
    print(a, b)

    x = y = z = 2021
    print(x, y, z)

    a = 1
    print(a, "is", type(a))
    a = "Hello Python"
    print(a, "is", type(a))
    print( isinstance(a, str))

def logical_oper():
    a, b = 20, 30
    print(not a < b)
    print(a < b and a != b)
    print(a == b or a != b)

def bit_oper():
    print(bin(5), bin(~5))

    bits = 1
    print(bin(bits))
    bits = bits << 4
    print(bin(bits))

    bits = 0b10101010
    print(bin(bits))
    print(bin(bits & 0b10))      # bit and
    print(bin(bits | 0b11111))   # bit or

if __name__ == "__main__":
    # arith_oper()
    # complex_ex()
    # rel_oper()
    # variable_ex()
    # assginment_ex()
    # logical_oper()
     bit_oper()

