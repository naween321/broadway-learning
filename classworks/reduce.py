from functools import reduce


# def summ(a, b):
#     return a + b


a = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, a)
print(result)
