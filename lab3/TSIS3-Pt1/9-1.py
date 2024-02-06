from math import pi
def sphere(r):
    V = (4*pi*r**3)/3
    return V
r = int(input())
volume = sphere(r)
print("volume of a sphere - ", volume)