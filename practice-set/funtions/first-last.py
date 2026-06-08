# Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".
def full_name(first, last):
    return first + " " + last

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
name = full_name(first_name, last_name)
print("Your full name is: " + name)
