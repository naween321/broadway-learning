# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""
#
#     if x == 1:
#         print("1 is returned")
#         return 1
#     else:
#         v = x * factorial(x-1)
#         print("v is returned")
#         return v
#
#
# num = 5
# if num < 10:
#     raise Exception("Error")
# print("The factorial of", num, "is", factorial(num))


# def summ(n):
#     if n <= 0:
#         return 0
#     else:
#         return (n % 10) + summ(n//10)
#
#
# print(summ(123))

class X:
    pass

class Y:
    a = "Y"

class Z:
    a = "Z"

class A(X, Z):
    pass

class B(Y):
    pass

class C(A, B):
    pass

o = C()
print(o.a)
