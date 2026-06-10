class Student:

    def getName(self,name):
        return name
    
input_name = input("Enter Name: ")
s1 = Student()
print("Student Name : ", s1.getName(input_name))
