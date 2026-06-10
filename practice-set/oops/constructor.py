# 2. Constructor and Attributes
# Create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes.
# Create an object and print the person’s name and age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name : ", self.name)
        print("Age : ", self.age)

p1 = Person("Dhanraj", 20)
p1.show()