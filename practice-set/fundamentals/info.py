name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in feets: "))  
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

print("Name:", name)
print("Age:", age)      
print("Height:", height)
print("Is Student:", is_student)