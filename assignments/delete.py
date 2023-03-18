import json
filename = 'students.json'


def delete(id):
    with open(filename, 'r') as fp:
        students = fp.read()
        students = json.loads(students)
    student = list(filter(lambda x: x['id'] == id, students))[0]
    students.remove(student)
    with open(filename, 'w') as fp:
        json.dump(students, fp)
    cont = input("The student is deleted. Do you want you want to continue? ")
    if cont.lower() == 'y':
        return True
    return False
