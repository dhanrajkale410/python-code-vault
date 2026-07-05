try:
    with open("dhanraj.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")

with open("hello.txt", "w") as file:
    file.write("Data written using 'with'.\n")