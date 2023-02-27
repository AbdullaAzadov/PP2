import math
n = float(input("Input number of sides: "))
l = float(input("Input the length of a side: "))

area = (n * (l**2) * (1/math.tan(math.radians(180/n)))) / 4
print("The area of this polygon is:", round(area, 2))