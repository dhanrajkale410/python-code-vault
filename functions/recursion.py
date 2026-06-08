# This code defines a recursive function to calculate the factorial of a given number. The user is prompted to enter a number, and the program then computes and displays the factorial of that number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number to calculate its factorial: "))
result = factorial(number)

print(f"The factorial of {number} is: {result}")
