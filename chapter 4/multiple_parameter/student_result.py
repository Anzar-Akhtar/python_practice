def student_result(name, english, maths, python):
    total = english + maths + python
    percentage = total / 3

    print("/nStudent Name:", name)
    print("Total Marks:", total)
    print("Percentage:", percentage)

    if percentage >= 45:
        print("Result: Pass")
    else:
        print("Result: Fail")


name = input("Enter student name: ")
english = int(input("Enter marks in English: "))
maths = int(input("Enter marks in Maths: "))
python = int(input("Enter marks in Python: "))

student_result(name, english, maths, python)