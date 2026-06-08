def greet(name, greeting="Hello"):
    print(greeting + ", " + name + "!")

user_name = input("Enter your name: ")
greet(user_name)  # Uses default greeting "Hello"

greet(user_name, "Hi")  # Uses custom greeting "Hi"
