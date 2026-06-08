# This module contains mathematical functions for various calculations.
import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

# Example usage:
radius = float(input("Enter the radius of the circle: "))

circle_area = calculate_circle_area(radius)

print(f"The area of the circle is: {circle_area}")

# Additional mathematical functions can be added here as needed.

def calculate_square_root(number):
    if number < 0:
        return "Cannot calculate square root of a negative number."
    else:
        return math.sqrt(number)
    
num = float(input("Enter a number to find its square root: "))
sqrt_result = calculate_square_root(num)
print(f"The square root of {num} is: {sqrt_result}")