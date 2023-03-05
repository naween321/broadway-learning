# filter(func, iterable)


a = [1, 2, 3, 4, 5, 6, 7, 8]


# def is_even(value):  # Return type is boolean True / False
#     return value % 2 == 0


result = list(filter(lambda x: x % 2 == 0, a))
print(result)


b = ["v", "a", "c", "d", "z", "e"]


# def is_vowel(value):
#     return value in ["a", "e", "i", "o", "u"]
#
#
result = list(filter(lambda x: x in ["a", "e", "i", "o", "u"], b))
print(result)

is_vowel = lambda value: value in ["a", "e", "i", "o", "u"]
print(is_vowel("b"))
