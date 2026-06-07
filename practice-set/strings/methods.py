"""
String Methods and Functions
Take the string " i love python programming " and:
Remove extra spaces from both ends
Convert it to title case
Count how many times "o" appears
Check if the string "123abc" is alphanumeric.
"""

str = " i love python programming "
# Remove extra spaces from both ends
str = str.strip()
print(str)  # Output: "i love python programming"

# Convert it to title case
str = str.title()
print(str)  # Output: "I Love Python Programming"

# Count how many times "o" appears
count_o = str.count("o")
print(count_o)  # Output: 3

# Check if the string "123abc" is alphanumeric
alphanumeric_str = "123abc"
is_alphanumeric = alphanumeric_str.isalnum()
print(is_alphanumeric)  # Output: True (since "123abc" contains only letters and numbers)