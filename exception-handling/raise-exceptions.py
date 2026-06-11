def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older!")
    return "Access granted."

age = int(input("Enter Age : "))

try:
  print(check_age(age))
except ValueError as e:
  print(f"Error: {e}")