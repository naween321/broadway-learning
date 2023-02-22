"""For the first 30 integers, print the number as it is as otherwise,
“Fizz” if the number is a multiple of 3, “Buzz” if the number is a multiple of 5 and
“FizzBuzz” if the number is the multiple of both 3 and 5.
"""
for i in range(30):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
