# # # def addition(a, b):
# # #     return a + b
# # #
# # #
# # # try:
# # #     first_num = int(input("Enter a number"))
# # #     second_num = int(input("Enter another number"))
# # # except ValueError:
# # #     print("Please enter numbers rather than string")
# # # else:
# # #     r = addition(first_num, second_num)
# # #     print(r)
# #
# #
# #
# # def division(a, b):
# #     try:
# #         return a/b
# #     except ZeroDivisionError:
# #         return "Cannot divide by zero"
# #
# #
# # try:
# #     first_num = int(input("Enter the first number "))
# #     second_num = int(input("Enter the second number "))
# # except ValueError:
# #     print("Please enter number")
# # else:
# #     r = division(first_num, second_num)
# #     print(r)
#
# student = {
#     "name": "Rohan",
#     "age": 23,
#     "department": "Computer"
# }
# information = input("Enter the key you want to access ")
# try:
#     print(f"The {information} of the student is {student[information]}")
# except KeyError:
#     print("Please input the valid key")
#

def is_vowel(char):
    if len(char.strip()) > 1:
        return "It is a word. Please enter a character"
    elif char.isnumeric():
        return "Please enter a character not a number"
    if char.lower().strip() in ['a', 'e', 'i', 'o', 'u']:
        return "Vowel"
    else:
        return "Not Vowel"

char = input("Enter a character ")
print(is_vowel(char))
