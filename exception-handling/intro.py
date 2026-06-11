n1 = int(input("Enter first Number : "))
n2 = int(input("Enter second Number : "))

try:
    res = n1 / n2
    print("Division :", res)
    
except ZeroDivisionError:
    print("Can't be divided by zero!")