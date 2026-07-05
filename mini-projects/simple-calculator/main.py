try:
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))

    o = input("Enter Operation (+,-,/,*) : ")

    match o:
        case "+":
            print("Addition : ", a + b)
        case "-":
            print("Subtraction : ", a - b)
        case "/":
            print("Division : ", a / b)
        case "*":
            print("Multiplication : ", a * b)
        
        case default:
            print("Invalid Operation!")

except Exception as e:
    print("Enter a Valid Value for Operation!")