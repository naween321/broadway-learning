# Take three numbers as a user input and find the greatest among them

a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
c = int(input("Enter the third number "))
if a > b and a > c:
    print(f"{a} is the greatest")
elif b > a and b > c:
    print(f"{b} is the greatest")
else:
    print(f"{c} is the greatest")
