question = [
                ["Which keyword is used to define a function in Python?", "function","define", "def", "fun", 3],
                ["Which of the following is used to take input from the user?", "print()", "input()", "scan()", "read()", 2],
                ["What is the correct file extension for Python files?", ".java", ".py", ".html", ".php", 2],
                ["Which data type is used to store True or False values?", "str", "int", "bool", "float", 3],
                ["Which symbol is used for comments in Python?", "//", "#", "/*", "--", 2]
             ]


print("Welcome to the Quiz Game!!")

for question in question: 
    print(f"{question[0]}")
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    answer = int(input("Enter your answer (1-4): "))

    if answer == question[5]:
        print("Correct answer!")
    else:
        print("Incorrect answer!")

    