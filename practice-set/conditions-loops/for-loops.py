# Practice Set 2.4 - Print numbers from 1 to 10 using a for loop
for i in range(1, 11):
    print(i)

# Practice Set 2.5 - Print the multiplication table of a given number
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

# Practice Set 2.6 - Calculate the sum of the first 100 natural numbers
total = 0
for i in range(1, 101):
    total += i
print("The sum of the first 100 natural numbers is:", total)

# Practice Set 2.7 - Print a right-angled triangle pattern of stars
for i in range(1, 5):
    print("*" * i)