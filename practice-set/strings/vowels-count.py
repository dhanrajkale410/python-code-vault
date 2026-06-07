# Write a program that counts how many vowels are in a given string.

string = "Hello, how are you doing today?"
vowels = "aeiouAEIOU"
count = 0

print("String:", string)

for char in string:
    if char in vowels:
        count += 1

print("Number of vowels:", count)