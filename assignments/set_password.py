import json

password = input("Please set your password ")
data = {"password": password}
with open("password.json", 'w') as fp:
    json.dump(data, fp, indent=4)
print("Password added successfully")
