def decorate_me(func):
    def inner_func(x, y):
        print("It is a decorated function")
        return func(x, y)
    return inner_func


@decorate_me
def summ(a, b):
    return a + b

@decorate_me
def diff(a, b):
    return a - b

print(summ(5, 4))
print(diff(5, 4))



# decorated = decorate_me(summ)
# print(decorated(2, 3))
