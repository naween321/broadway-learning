# for i in range(10):  # it ranges from 0 to 9
#     print(i)
#
#
# for i in range(1, 11):
#     print(i)

# Find the even numbers from the first 10 natural numbers
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)


"""for the first 30 natural numbers print the number as it is; if otherwise divisible by 3 print
'Fizz', if divisible by 5 print 'Buzz', if divisible by both 3 and 5 print 'FizzBuzz' """

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
        break
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")

