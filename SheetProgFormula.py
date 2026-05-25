# Q1 Area of Rectangle
length, breadth = 10, 5
print(length * breadth)

# Q2 Area of Square
side = 4
print(side * side)

# Q3 Area of Triangle
base, height = 10, 5
print(0.5 * base * height)

# Q4 Area of Circle
import math
radius = 7
print(math.pi * radius ** 2)

# Q5 Distance between two points
x1, y1 = 0, 0
x2, y2 = 3, 4
print(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

# Q6 Fahrenheit to Celsius
fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F = {celsius:.2f}°C")

# Q7 Celsius to Fahrenheit
celsius = 37
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit:.2f}°F")

# Q8 Perimeter of a Square
side = 5
print("Perimeter of Square:", 4 * side)

# Q9 Perimeter of a Rectangle
length, breadth = 10, 6
print("Perimeter of Rectangle:", 2 * (length + breadth))

# Q10 Perimeter of a Triangle
a, b, c = 3, 4, 5
print("Perimeter of Triangle:", a + b + c)

#Q11 Circumference of a Circle
radius = float(input("Enter the radius of the circle: "))
print("Circumference of Circle:", 2 * math.pi * radius)

#Q12: Surface Area, Volume, and Perimeter of a Cube
#surface area = 6 * side^2
#volume = side^3
#perimeter = 12 * side
side = int(input("Enter the side length of the cube: "))
surface_area = 6 * side ** 2
volume = side ** 3
perimeter = 12 * side
print("Surface Area of Cube:", surface_area)
print("Volume of Cube:", volume)
print("Perimeter of Cube:", perimeter)

#Q13 Surface Area and Volume of a Cuboid
# surface area = 2(lb + bh + hl)
# volume =lbh

length = int(input("Enter the length of the cuboid: "))
breadth = int(input("Enter the breadth of the cuboid: "))
height = int(input("Enter the height of the cuboid: "))
surface_area = 2 * (length * breadth + breadth * height + height * length)
volume = length * breadth * height
print("Surface Area of Cuboid:", surface_area)
print("Volume of Cuboid:", volume)

#14 Surface Area and Volume of a Sphere
# surface area = 4* pi * r ** 2
# volume = 4/3 * pi * r ** 3
radius = int(input("Enter the radius of the sphere: "))
surface_area = 4 * math.pi * (radius ** 2)
volume = (4/3) * math.pi * (radius ** 3)

print("Surface Area of Sphere =", surface_area)
print("Volume of Sphere =", volume)

#Q15 Surface Area and Volume of a Cylinder
# surface area = 2 * pi * r * (r + h)
# volume = pi * r ** 2 * h
radius = int(input("Enter the radius of the cylinder: "))
height = int(input("Enter the height of the cylinder: "))
surface_area = 2 * math.pi * radius * (height + radius)
volume = math.pi * (radius ** 2) * height
print("Surface Area of Cylinder =", surface_area)
print("Volume of Cylinder =", volume)