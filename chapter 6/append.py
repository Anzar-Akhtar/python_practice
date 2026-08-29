name = input("Enter student name: ")

with open("student.txt", "a") as file:
    file.write(name + "\n")

file.close()

print("Student added successfully!!")