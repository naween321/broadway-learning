s = "Delete all occurrences of a specified character in a given string"
to_remove = input("Enter the character to remove ")
result = ''
for each in s:
    if each.lower() == to_remove.lower():
        continue
    result += each
print(result)
