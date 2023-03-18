import json

filename = 'students.json'


def update(id, to_change, changed_info):
    with open(filename, 'r') as fp:
        students = fp.read()
        students = json.loads(students)
    student = list(filter(lambda x: x['id'] == id, students))
    student = student[0]
    student_index = students.index(student)
    students[student_index][to_change] = changed_info
    with open(filename, 'w') as fp:
        json.dump(students, fp)
    cont = input("Student updated successfully. Do you want you want to continue? ")
    if cont.lower() == 'y':
        return True
    return False
