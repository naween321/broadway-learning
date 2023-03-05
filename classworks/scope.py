a = 1  # Global scope


# def test(a, b=1):
#     print(a)
#     print(b)
#
# test()


# def summ(b, c, d=1, *args, **kwargs):  # b, c, d and e are arguments
#     global a
#     print("Value of d is", d)
#     a = 2
#     print("Inside Function", a)
#     return b + c
#
#
# print("Outside function", a)
# # print(summ(2, 3))
# summ(2, 3)  # here 2 and 3 are parameters
# print("Outside function", a)


def summ(a, b, c, d=1, e=2, *args, **kwargs):
    print(kwargs)  # {"a": 1, "b":2, "c": 3}
    print(type(kwargs))
    return sum(kwargs.values())


summ(1, 2, 3, 4, 5, 6, 7, 8, 3, 4, a=9, b=10)
