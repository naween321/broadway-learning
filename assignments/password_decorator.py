import json


def password_required(func):
    def inner_func(*args, **kwargs):
        password = input("Please enter the password ")
        with open("password.json", 'r') as fp:
            data = fp.read()
            data = json.loads(data)
        if data['password'] == password:
            print("Permission Granted !!")
            return func(*args, **kwargs)
        else:
            print("Sorry!!, you don't have access")
    return inner_func
