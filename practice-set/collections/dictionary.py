# Dictionaries and Dictionary Methods
# Create a dictionary student = {"name": "John", "age": 20, "grade": "A"} and:

    # Print the value of "name".
    # Change "grade" to "A+".
    # Add a new key "city" with value "Delhi".

student = {"name": "John", "age": 20, "grade": "A"}

value_name = student.get("name")
print(value_name)               # Print the value of "name".

student.update({"grade":"A+"})  # Change "grade" to "A+".    
print(student)

student.update({"city":"Delhi"}) # Add a new key "city" with value "Delhi".   
print(student)

# Create a dictionary of three friends and their phone numbers. Use:
    # keys() to get all names
    # values() to get all numbers
    # items() to loop over key-value pairs and print them

numbers = {
    "Alice":8723839,
    "Alex": 7268302,
    "Maxwell": 827912
}

print(numbers.keys())            # keys() to get all names
print(numbers.values())          # values() to get all numbers
print(numbers.items())          # items() to loop over key-value pairs and print them