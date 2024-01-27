def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(5, 5, 6, 56, 8, 10, 2, 4, 3, 1)


def calculate(n,**kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["mul"]
    print(n)


calculate(2,add=3, mul=5)
