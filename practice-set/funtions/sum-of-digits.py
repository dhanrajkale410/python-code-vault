# Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)

number = int(input("Enter a number to calculate the sum of its digits: "))
result = sum_of_digits(number)

print(f"The sum of the digits of {number} is: {result}")