class Circle:
    def __init__(self, radius):
        self.radius = radius

    # def __gt__(self, other):
    #     return self.radius > other.radius

    def __str__(self):
        return f"Circle object with radius {self.radius}"


c1 = Circle(3)
c2 = Circle(5)
print(c2 > c1)
print(c1)