# file1 = open("test.txt", 'w')
# file1.write("Hello World")
# file1.close()

# file = open("test.txt", 'r')
# print(file.read())
# file.close()


with open("test.txt", 'r') as file:
    print(file.read())