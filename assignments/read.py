import json
filename = 'students.json'


def read(id):
    with open(filename, 'r') as fp:
        students = fp.read()
        students = json.loads(students)
    student = list(filter(lambda x: x['id'] == id, students))
    print(student)
    cont = input("Do you want you want to continue? ")
    return cont.lower() == 'y'
