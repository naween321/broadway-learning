class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __add__(self, obj):  # Dunder Method or Magic Method
        return self.radius + obj.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __str__(self):
        return f"Circle object with radius {self.radius}"


c1 = Circle(5)
c2 = Circle(10)
# result = c1.radius + c2.radius
# result = c1.__add__(c2)
print(c1.radius)
if c1 < c2:  # This is equivalent to c1.__gt__(c2)
    raise Exception("c1 cannot be greater")
