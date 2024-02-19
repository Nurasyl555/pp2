import math
number = float(input("Input number of sides: "))
length = float(input("Input the length of a side: "))
area = ((length**2)*number)/(4*math.tanh(180/number))
print(f"The area of the polygon is: {area}")

