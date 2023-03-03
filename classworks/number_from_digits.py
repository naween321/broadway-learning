# def number_from_digits(a):
#     number = 0
#     for i in a:
#         number = number * 10 + i
#     return number
#
#
# a = [1, 2, 3, 4, 5, 6, 7]
# result = number_from_digits(a)
# print(result)
#
#
# def custom_sort(a):   # Bubble Sort
#     length = len(a)
#     for i in range(length - 1):
#         for j in range(i + 1, length):
#             if a[i] > a[j]:
#                 a[i], a[j] = a[j], a[i]
#     return a
#
#
# a = [54, 1, 99, 20, 3]
# b = [1, 5, 0, 100, 20]
# r1 = custom_sort(a)
# r2 = custom_sort(b)
# print(r1)


def repeated_items(a):
    result = []
    for i in a:
        if a.count(i) > 1 and i not in result:
            result.append(i)
    return result


r = repeated_items([3, 4, 2, 2, 1, 3, 3, 3])
print(r)
