b = ["v", "a", "c", "d", "z", "e"]


# def capitalize(value):
#     return value.upper()  # V


result = list(filter(lambda x: x.upper(), b))
print(result)
