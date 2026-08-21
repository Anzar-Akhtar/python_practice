students = {
    "Anzar": 85,
    "Atah": 90,
    "Aaira": 95
}

marks_list = list(students.values())

avg = sum(marks_list) / len(marks_list)
max_marks = max(marks_list)
min_marks = min(marks_list)

print("Average Marks:", avg)
print("Maximum Marks:", max_marks)
print("Minimum Marks:", min_marks)