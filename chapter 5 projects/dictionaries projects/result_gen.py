students = {}

print("Enter details for 5 students: ")
for i in range(5):
    name = input(f"Enter student {i+1} name: ")
    marks = int(input(f"Enter marks of {name}: "))
    students[name] = marks

print("\n--- Result ---")
for name, marks in students.items():
    if marks >= 45:
        result = "PASS"
    else:
        result = "FAIL"

    print(f"{name}: {marks} marks -> {result}")