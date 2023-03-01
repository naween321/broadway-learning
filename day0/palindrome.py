"""
Check whether an integer (not string) is palindrome or not.
Input: 123
Output: “Not Palindrome”
"""

n = 122
check_n = n
reversed_num = 0
while n != 0:
    last_term = n % 10
    reversed_num = reversed_num * 10 + last_term
    n = n // 10
if check_n == reversed_num:
    print("Palindrome")
else:
    print("Not Palindrome")

print("My new feature")
