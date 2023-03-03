s = "All the occurrences of a specified character in a given string"
a = input("Enter the character to be removed ")
result = ""
for each in s:
    if each.lower() == a.lower():
        continue
    result = result + each

print(result)

# [1, 2, 3, 4]
# 123
#
# 1*10 + 2 = 12
# 12 * 10 + 3 = 123
# 123 * 10 + 4 = 124

