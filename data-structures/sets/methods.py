my_set = {1, 2, 3, 4}
 
my_set.add(5)        # add() - Adds an element to the set
print(my_set)        # {1, 2, 3, 4, 5}

my_set.remove(2)     # remove() - Removes the specified element
print(my_set)        # {1, 3, 4, 5}

my_set.discard(10)   # discard - Remove the specified item
print(my_set)        # No error if element not found

my_set.pop()         # Removes random element
print(my_set)