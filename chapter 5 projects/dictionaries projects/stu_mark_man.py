students = {}

print("Enter details for 5 students: ")
for i in range(5):
    name = input(f"Enter student {i+1} name: ")
    marks = int(input(f"Enter marks of {name}: "))
    students[name] = marks


marks_list = list(students.values())


avg = sum(marks_list) / len(marks_list)
max_marks = max(marks_list)
min_marks = min(marks_list)

print("\nStudents dictionary:", students)
print("Average marks:", avg)
print("Maximum marks:", max_marks)
print("Minimum marks:", min_marks)