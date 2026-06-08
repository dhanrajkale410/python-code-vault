# Introduction to Tuples in Python
my_tuple = (10, 20, 30)
print(my_tuple)  # Output: (10, 20, 30)
print(type(my_tuple))  # Output: <class 'tuple'>

# Tuple Unpacking
a, b, c = my_tuple
print(a)  # Output: 10
print(b)  # Output: 20
print(c)  # Output: 30

# Tuples can contain different data types
mixed_tuple = (1, "Hello", 3.14)
print(mixed_tuple)  # Output: (1, 'Hello', 3.14)
print(type(mixed_tuple))  # Output: <class 'tuple'>

# Creating a tuple with a single element
single_element = (5,)  # Tuple with one element (comma required)
print(single_element)  # Output: (5,)
print(type(single_element))  # Output: <class 'tuple'>