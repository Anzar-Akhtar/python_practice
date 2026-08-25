marks = []

print("Enter marks for 5 students: ")
for i in range(5):
    m = int(input(f"Student {i+1} marks: "))
    marks.append(m)

total = sum(marks)
avg = total / len(marks)
high = max(marks)
low = min(marks)

print("\nMarks list:", marks)
print("Total marks:", total)
print("Average marks:", avg)
print("Highest marks:", high)
print("Lowest marks:", low)