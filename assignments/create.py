import os
import json
from password_decorator import password_required
filename = 'students.json'


@password_required
def create():
    id = input("Enter id of the student ")
    name = input("Enter name of the student ")
    dept = input("Enter the department of the student ")
    student = dict(id=id, name=name, department=dept)
    if os.path.exists(filename):
        with open(filename, 'r') as fp:
            students = json.load(fp)
    else:
        students = []
    students.append(student)
    with open(filename, 'w') as fp:
        json.dump(students, fp, indent=2)
    cont = input("A new student added. Do you want you want to continue? ")
    if cont.lower() == 'y':
        return True
    return False
