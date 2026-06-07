# prints the numbers from 1 to 10 using a while loop.
i = 1
while i < 11:
    print(i)
    i += 1

# calculates the factorial of a given number using a while loop.
num = int(input("Enter a number to calculate its factorial: "))
factorial = 1
while num > 1:
    factorial *= num
    num -= 1
print("The factorial is:", factorial)

# Password validation using a while loop.
correct_password = "python123"
while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")

# Reverses a number using a while loop.
number = int(input("Enter a number to reverse: "))
reversed_number = 0
while number > 0:
    digit = number % 10 
    reversed_number = reversed_number * 10 + digit
    number //= 10
print("The reversed number is:", reversed_number)
