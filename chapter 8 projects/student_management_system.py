students = []

def add_students():
        print("\n==== ADD STUDENTS ====\n")

        id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        student = {
            "ID": id,
            "Name": name,
            "Age": age,
            "Course": course,
            "Marks": marks
        }

        students.append(student)
        print(students)

def view_all_students():
    print("\n==== STUDENTS LIST ====\n")

    if(len(students) == 0):
        print("No Student Available!")

    else:
        for student in students:
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])
            print("Marks:", student["Marks"])

def search_students():
    print("\n==== VIEW STUDENTS ====\n")

    search_id = int(input("Enter the ID of the student you wants to search: "))

    found = False
    for student in students:
        if(search_id == student["ID"]):
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])
            print("Marks:", student["Marks"])

            found = True

    if found == False:
        print("Student Not Found!")

def update_student():
    pass

while True:
    print("\n==== STUDENT MANAGEMENT SYSTEM ====\n")
    print("1. Add Students")
    print("2. View All Students")
    print("3. Search Students")
    print("4. Update Students")
    print("5. Delete Students")
    print("6. Calculate Average Marks")
    print("7. Find Topper")
    print("8. Display Failed Students")
    print("9. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_students()

    elif choice == "2":
        view_all_students()

    elif choice == "3":
        search_students()

    
    elif choice == "9":
        break