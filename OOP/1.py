# class Vehicle:
#     def __init__(self, doors):
#         self.doors = doors
#
#
# class Bike(Vehicle):
#     def __init__(self, doors, wheels):
#         self.wheels = wheels
#         super().__init__(doors)
#
# # v = Vehicle(4)
#
# b = Bike(0, 2)
#
# print(b.doors)

class X:
    def first(self):
        return "First from X is called"
class A(X):
    b = 1

class B:
    def first(self):
        return "First fro B is called"

class C(A, B):
    a = 1

obj = C()
print(obj.first())
