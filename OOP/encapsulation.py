class Vehicle:
    def __init__(self):
        self.color = 'red'
        """This is a protected memeber"""
        self._mileage = 99
        self.__doors = 4

    # def change_mileage(self, mileage):
    #     self._mileage = mileage


my_vehicle = Vehicle()

"""Cant access private members in this way"""
print(my_vehicle.__doors)

"""Can access protected member in this way but not recommended"""
print(my_vehicle._mileage)

"""This is called name mangling. Can access even the private members"""
print(my_vehicle._Vehicle__doors)
# my_vehicle.change_mileage(25)
# my_vehicle.change_mileage(100)
# print(my_vehicle._mileage)
#
# """This is also possible but not recommended"""
# my_vehicle._mileage = 10
# print(my_vehicle._mileage)
