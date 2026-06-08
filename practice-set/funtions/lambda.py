# Lambda Functions
# Write a lambda function that adds two numbers and test it.
# Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.
add = lambda x, y: x + y
print(add(5, 3))

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)