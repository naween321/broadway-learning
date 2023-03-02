n = int(input("Enter a number "))
summ = 0
new_n = 0
for _ in range(n):
    new_n = new_n * 10 + n
    print(new_n)
    summ = summ + new_n
print("Sum is ", summ)
