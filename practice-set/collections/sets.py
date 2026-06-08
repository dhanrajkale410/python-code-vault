#  Sets and Set Methods
# Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3?)
# Add 5 to the set, remove 2, and check if 4 is in the set.

my_set = {1, 2, 3, 3, 4}

print(my_set)

my_set.add(5)
my_set.remove(2)
print(my_set)

# Create two sets:
# a = {1, 2, 3}
# b = {3, 4, 5}
# Find their:
    # Union
    # Intersection
    # Difference (a - b)

a = {1, 2, 3}
b = {3, 4, 5}

print(a)
print(b)

print(a.union(b))               # Union
print(a.intersection(b))        # Intersection
print(a.difference(b))          # Difference (a - b)