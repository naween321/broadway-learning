class Vehicle:
    def __init__(self, d, color):
        self.doors = d
        self.color = color


class Bike(Vehicle):  # This is single inheritance
    def __init__(self, doors, color, wheels):
        self.wheels = wheels
        super().__init__(doors, color)


class Car(Vehicle):
    # This is  called method overriding
    def __init__(self, doors, color, mileage):
        self.mileage = mileage
        super().__init__(doors, color)

    """
    if we do not add __init__ method in the child class then the __init__ from
    parent class is called
    """

honda = Bike(0, 'red', 2)
rover = Car(4, 'blue', 25)

print(honda.doors)
print(honda.color)
print(rover.mileage)
print(rover.doors)

