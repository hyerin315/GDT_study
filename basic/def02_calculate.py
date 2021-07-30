import math

def calcultate_area(radius):
    area = math.pi * radius**2
    return area

r = float(input("Input radius of circle : "))
print(calcultate_area(r))

