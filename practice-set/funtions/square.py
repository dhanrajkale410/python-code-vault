# Write a function calculate_square() that takes a number as an argument and returns its square.
def calculate_square(number):
    return number ** 2  

num = float(input("Enter a number to find its square: "))

result = calculate_square(num)

print(f"The square of {num} is: {result}")