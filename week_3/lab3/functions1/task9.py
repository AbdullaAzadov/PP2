import math
def volume(radius):
    v = 4/3 * math.pi * radius**3
    return v

radius = float(input("Radius of the sphere: "))    
print(round(volume(radius), 2))
