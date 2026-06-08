# Tuples and Operations on Tuples
    # Create a tuple coordinates = (10, 20) and print both elements.
    # Try to modify the tuple by setting coordinates[0] = 50 — note what happens.
    # Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.

coordinates = (10, 20)
print(coordinates)      # Create a tuple coordinates = (10, 20) and print both elements.

# coordinates[0] = 50
# print(coordinates)      # TypeError: 'tuple' object does not support item assignment

list1 = list(coordinates)

print(list1)
print(type(list1))
