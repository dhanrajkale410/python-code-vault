n1 = int(input("Enter first Number : "))
n2 = int(input("Enter second Number : "))

try:
    res = n1 / n2
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")