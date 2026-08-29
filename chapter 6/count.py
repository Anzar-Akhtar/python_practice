with open("student.txt", "r") as file:
    students = file.readline()

file.close()
print("Total students:", len(students))