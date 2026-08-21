student = {}

print("Enter details for 3 students:")
for i in range(3):
    name = input(f"Enter name of student {i + 1}: ")
    marks = int(input(f"Enter marks of student {name}: "))
    student[name] = marks

print("\nStudents Dictionary:", student)