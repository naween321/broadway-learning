n = int(input("Enter a number "))
new_n = 0
summ = 0
for _ in range(n):
    new_n = new_n * 10 + n  # => 5 * 10 + 5 = 555
    summ = summ + new_n  # 60 + 555 = 625

print(summ)

# 5 + 55 + 555 + 5555 + 55555
# n1 = int(input("Enter a number "))
# n2 = int(input("Enter another number "))
# summ = n1 + n2
#
# if summ > 15 and summ < 20:
#     print(20)
# else:
#     print(summ)
#
# if summ in range(16, 20):
#     print(20)
# else:
#     print(summ)
