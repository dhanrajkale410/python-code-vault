a = {1, 2, 3}
b = {3, 4, 5}

print(a)
print(b)

# union() - Return a set containing the union of sets 
print(a.union(b))       # {1, 2, 3, 4, 5}

# intersection() - Returns a set, that is the intersection of two other sets
print(a.intersection(b))  # {3}

# difference() - Returns a set containing the difference between two or more sets
print(a.difference(b))   # {1, 2}