name = "Dhanraj"

#   D     H   A   N   R   A   J
#   0     1   2   3   4   5   6 
#  -1    -2  -3  -4  -5  -6   -7 

# Slicing syntax: string[start:end:step]
# start: The index to start the slice (inclusive)
# end: The index to end the slice (exclusive)
# step: The step size for slicing (optional)

# Extracting "Dhan" from "Dhanraj"
slice1 = name[0:4]  # Dhan  
print(slice1)

# Extracting "raj" from "Dhanraj"
slice2 = name[4:7]  # raj   
print(slice2)

# Extracting "Dhanraj" using slicing
slice3 = name[0:7]  # Dhanraj
print(slice3)   


# Negative indexing with slicing
# Extracting "Dhan" using negative indexing
slice4 = name[-7:-3]  # Dhan
print(slice4)

# Extracting "raj" using negative indexing
slice5 = name[-3:]  # raj
print(slice5)

# Extracting "Dhanraj" using negative indexing
slice6 = name[-7:]  # Dhanraj
print(slice6)