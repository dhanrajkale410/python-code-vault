class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print("Name : ", self.name)
        print("Marks : ",self.marks)

s1 = Student("Dhanraj", 99.99)
print(s1.show())
