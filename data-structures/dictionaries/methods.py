student = {"name": "Alice", "age": 21, "grade": "A"}

# keys() - Returns a list containing the dictionary's keys
print(student.keys())    # dict_keys(['name', 'age', 'grade', 'city'])

# values() - Returns a list of all the values in the dictionary
print(student.values())  # dict_values(['Alice', 22, 'A', 'New York'])

# items() - Returns a list containing a tuple for each key value pair
print(student.items())   # dict_items([('name', 'Alice'), ('age', 22), ...])

# pop() - Removes the element with the specified key
student.pop("age")  # Removes "age" key

student.clear()  # Empties dictionary