with open("welcome.txt", "w") as file:
    file.write("Welcome to Python")

print("File created successfully!!")

with open("welcome.txt", "r") as file:
    data = file.read()

print(data)
file.close()