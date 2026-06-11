age = int(input("Enter Age : "))

class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    def __init__(self, message="Age must be 18 or older!"):
        self.message = message
        super().__init__(self.message)

def verify_age(age):
    if age < 18:
        raise InvalidAgeError()  # Raise your custom exception
    return "Welcome!"


try:
    print(verify_age(age))
    
except InvalidAgeError as e:
    print(f"Error: {e}")