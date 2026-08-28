stu1 = set(
    input("Enter Student 1 Subjects: ").split()
)

stu2 = set(
    input("Enter Student 2 Subjects: ").split()
)

print("\n--- Subject Analysis ---")

print("common sunjects:", stu1 & stu2)
print("Student 1 subjects:", stu1 - stu2)
print("Student 2 subjects:", stu2 - stu1)