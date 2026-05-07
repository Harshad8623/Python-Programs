# Write a program to find Area of Triangle

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)


# Another way to find Area of Triangle using function
def calculate_triangle_area(base, height):
    return 0.5 * base * height
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = calculate_triangle_area(base, height)
print("The area of the triangle is:", area)



# Another way to find Area of Triangle using Heron's formula
import math
side1 = float(input("Enter the length of the first side of the triangle: "))
side2 = float(input("Enter the length of the second side of the triangle: "))
side3 = float(input("Enter the length of the third side of the triangle: "))
s = (side1 + side2 + side3) / 2
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
print("The area of the triangle is:", area)



# Another way to find Area of Triangle using a class
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
triangle = Triangle(base, height)
print("The area of the triangle is:", triangle.area())



# Another way to find Area of Triangle using a lambda function
calculate_triangle_area_lambda = lambda base, height: 0.5 * base * height
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = calculate_triangle_area_lambda(base, height)
print("The area of the triangle is:", area)


# Another way to find Area of Triangle using a match case
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
match (base, height):
    case (b, h) if b > 0 and h > 0:
        area = 0.5 * base * height
        print("The area of the triangle is:", area)
    case _:
        print("Invalid input: Base and height must be positive numbers.")



# Another way to find Area of Triangle using a map function
def calculate_area(base, height):
    return 0.5 * base * height
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = map(lambda b, h: calculate_area(b, h), [base], [height])
print("The area of the triangle is:", list(area)[0])



# Another way to find Area of Triangle using a list comprehension
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = [0.5 * base * height for _ in range(1)][0]
print("The area of the triangle is:", area)