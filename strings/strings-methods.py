# String Methods

# Length Function
from os import name


str = "Dhanraj Kale"

print(len(str))  # Output: 13

# String Methods
print(str.upper())  # Output: DHANRAJ KALE

print(str.lower())  # Output: dhanraj kale

print(str.title())  # Output: Dhanraj Kale

print(str.strip())  # Output: Dhanraj Kale (removes leading/trailing whitespace)

print(str.replace("Dhanraj", "Raj"))  # Output: Raj Kale  

print(str.split())  # Output: ['Dhanraj', 'Kale'] (splits into a list of words)

print(str.find("Kale"))  # Output: 8 (index of the substring "Kale")

print(str.startswith("Dhan"))  # Output: True (checks if the string starts with "Dhan")

print(str.endswith("Kale"))  # Output: True (checks if the string ends with "Kale")    

print(str.count("a"))  # Output: 2 (counts occurrences of "a") 


