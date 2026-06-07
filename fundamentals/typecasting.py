# Implicit Type Conversion
a = 5
b = 2.5
result = a + b  # a is implicitly converted to float
print("Result of a + b:", result)   
print("Type of result:", type(result))   # Output: <class 'float'>

# Explicit Type Conversion
x = 10  
y = 3
division_result = x / y  # This will be a float
print("Division Result:", division_result)  # Output: 3.3333333333333335
print("Type of division_result:", type(division_result))  # Output: <class 'float'> 

# Now we want to convert the division result to an integer
integer_result = int(division_result)  # Explicitly converting to integer   
print("Integer Result:", integer_result)  # Output: 3
print("Type of integer_result:", type(integer_result))  # Output: <class 'int'> 
