mark_list = []

print("Enter marks for 5 subjects: ")
for i in range(5):
    m = int(input(f"Enter Subject {i+1} marks: "))
    mark_list.append(m)

mark_tuple = tuple(mark_list)

total = sum(mark_tuple)
avg = total / len(mark_tuple)
max_mark = max(mark_tuple)
min_mark = min(mark_tuple)

print("\nMarks tuple:", mark_tuple)
print("Total:", total)
print("Average:", avg)
print("Maximum:", max_mark)
print("Minimum:", min_mark)