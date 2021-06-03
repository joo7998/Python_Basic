def bool_ex():
    print (bool(0), bool(1))
    # 0 = false , 1 = true

    a = 1
    print(a > 10)

    b = a == 1
    print(b, type(b))

    print(b + 10)

    print(isinstance(True, bool))
    print(isinstance(True, int))

    # boolean casting
    # 0 = empty = false
    print(bool(10), bool(0))
    print(bool(3.14), bool(0.0))
    print(bool("Python"), bool(""))
    print bool([1, 2, 3]), bool([])
    print bool({"a": 2}), bool({})
    print bool(None)

    # Circuit Break
    print([1, 2, 3] or []) # OR : first True
    print([] or [1, 2, 3])
    print([1, 2, 3] and [4, 5, 6]) # AND : if both true -> latter
    print([1, 2, 3] and []) # AND : if false -> None

def integer_ex():
    a = 23
    b = int(23)
    print(a, type(a))
    print(b, isinstance(b, int))

    b = 0b1101 # binary = 0b
    o = 0o23   # oct = 0o
    x = 0xFF   # hex = 0x

    print(b, o, x)

    i = 2 ** 2048
    print(i)
    print(i.bit_length())

    print(bin(2021))
    print(oct(2021))
    print(hex(2021))

def float_ex():
    a = 3.1459
    print(a, type(a))
    b = float(3.0)
    print(b, isinstance(b, float))
    print(a.is_integer(), b.is_integer())
    # int = number without floating point
    # is_integer : type X, whether the value is int

    c = 3e3         # 3 * 10 ** 3
    d = -2E-5       # -2 * 10 ** -5
    print(c, d)
    print(-2E-5 == -0.00002)

def complex_ex():
    a = 4 + 5j
    print(a, type(a))
    b = 7-2J
    print(b, isinstance(b, complex))

    print(a + b)

    print(a, a. real)  # real number
    print(a, a.imag)   # imaginary number
    print(a, a.conjugate())

    c = 7
    d = 3
    e = complex(7, 3)
    print(e, type(e))

def builtin_math_function():
    print(abs(-1))
    print(int(3.14159))
    print(float(3))
    print(complex(1))
    print(divmod(5, 3))
    print(pow(2, 4))






if __name__ == "__main__":
    # bool_ex()
    # integer_ex()
    # float_ex()
    # complex_ex()
    builtin_math_function()