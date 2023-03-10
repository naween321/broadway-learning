class X:
    def display(self):
        return "I am message from class X"

class A(X):
    b = 1
    # def display(self):
    #     return "I am message from class A"

class B:
    def display(self):
        return "I am message from class B"


"""
This is multiple inheritance
"""
class C(A, B):
    __a = 1  # Protected attribute
    def _display(self):
        return "I am message from C"

    def access_a(self):
        return self.__a

obj = C()
print(obj.display())
print(obj.access_a())

"""
Inheritance
Encapsulation
Abstraction
Polymorphism
"""