n1 = int(input("Enter a number "))
n2 = int(input("Enter another number "))
summ = n1 + n2

if summ > 15 and summ < 20:
    print(20)
else:
    print(summ)

if summ in range(16, 20):
    print(20)
else:
    print(summ)
