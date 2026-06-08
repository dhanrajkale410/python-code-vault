# Lambda function to calculate the square of a number
square = lambda x: x ** 2

number = float(input("Enter a number: "))

result = square(number)

print("The square of the number is: ", result)  

# Lambda function to add two numbers
add = lambda a, b: a + b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = add(num1, num2)

print("The sum of the two numbers is: ", result)
