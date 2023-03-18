from functools import reduce
class Department:
    def __init__(self, name, number_of_students):
        self.name = name
        self.number_of_students = number_of_students

    def total_students(self, obj):
        # print(args)
        # other_total = reduce(lambda x, y: x.number_of_students+ y.number_of_students, args)  # (obj1.nu, obj2.nu, obj3)
        # list_of_nums = [i.number_of_students for i in args]   # (5.num, obj3.num)
        # other_total = sum(list_of_nums)
        return self.number_of_students + obj.number_of_students



d1 = Department("Sports", 20)
d2 = Department("Account", 12)
d3 = Department("Account", 32)
d4 = Department("Account", 11)
d5 = Department("Account", 21)
result = d1.total_students(d2, d3, d4, d5)
print(result)