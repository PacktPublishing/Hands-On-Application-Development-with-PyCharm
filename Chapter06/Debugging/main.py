def foo():
    a[1] = 3


if __name__ == '__main__':
    a = [0, 1, 2]
    b = a

    foo()

    print(a)
    print(b)
