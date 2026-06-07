"""
String Formatting and f-Strings
Using format() , create a sentence:
"My name is John and I am 25 years old."
by passing "John" and 25 as variables.
Do the same using f-strings.
"""

name = "John"
age = 25
# Using format()
sentence_format = "My name is {} and I am {} years old.".format(name, age)
print(sentence_format)  # Output: My name is John and I am 25 years old

# Using f-strings
sentence_f_string = f"My name is {name} and I am {age} years old."
print(sentence_f_string)  # Output: My name is John and I am 25 years old.