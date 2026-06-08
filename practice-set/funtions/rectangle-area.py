# Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

# Both length and width
# Only length (use default width)

def calculate_area(length, width=10):
    return length * width   

length = float(input("Enter the length of the rectangle: "))
# Test with both length and width
width = float(input("Enter the width of the rectangle: "))
area = calculate_area(length, width)

print(f"The area of the rectangle with length {length} and width {width} is: {area}")

# Test with only length (use default width)
area_default_width = calculate_area(length) 
print(f"The area of the rectangle with length {length} and default width 10 is: {area_default_width}")
