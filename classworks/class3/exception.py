def addition(a, b):
    try:
        r = a + b
        return r
    except TypeError:
        return "Please enter data with same type"


first_num = input("Enter a number")
second_num = input("Enter another number")
r = addition(first_num, second_num)
print(r)
