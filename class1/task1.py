import math
x1 = float(input("Enter x1 "))
x2 = float(input("Enter x2 "))
y1 = float(input("Enter y1 "))
y2 = float(input("Enter y2 "))

distance = ((x2-x1) ** 2 + (y2-y1) ** 2) ** (1/2)
print("Distance is ", distance)
d = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
print("Distance is ", d)
