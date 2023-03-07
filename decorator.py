def decorate_me(func):
    def inner_func(x, y):
        print("It is a decorated function")
        return func(x, y)
    return inner_func


def summ(a, b):
    return a + b


decorated = decorate_me(summ)
print(decorated(2, 3))
