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
    print("\n==== UPDATE STUDENT ====\n")

    upd_stu_id = int(input("Enter the ID of the student you want to update: "))

    found = False
    for student in students:
        if(upd_stu_id == student["ID"]):
            new_id = int(input("Enter the Updated ID: "))
            new_name = input("Enter the Updated Name: ")
            new_age = int(input("Enter the Updated Age: "))
            new_course = input("Enter the Updated Course: ")
            new_marks = float(input("Enter the Updated Marks: "))

            student["ID"] = new_id
            student["Name"] = new_name
            student["Age"] = new_age
            student["Course"] = new_course
            student["Marks"] = new_marks

            print("\n====Student Updated Successfully!====\n")
            
            print("Updated Student ID: ", student["ID"])
            print("Updated Name: ", student["Name"])
            print("Updated Age: ", student["Age"])
            print("Updated Course: ", student["Course"])
            print("Updated Marks: ", student["Marks"])

            found = True

    if found == False:
        print("Student Not Found!")

def delete_student():
    print("\n==== DELETE STUDENT ====\n")

    delete_id = int(input("Enter the Student ID you want to delete: "))

    found = False

    for student in students:
        if delete_id == student["ID"]:
            students.remove(student)

            found = True

            print("\nStudent Deleted Successfully\n")

    if found == False:
        print("Student Not Found!")

def calc_avg():
    print("\n==== CALCULATE AVERAGE MARKS ====\n")

    if len(students) == 0:
        print("No Student Available!")
    
    else:
        total_marks = 0

        for student in students:
            total_marks += student["Marks"]

        avg = total_marks / len(students)

        print("Average Marks: ", avg)

def find_topper():
    print("\n==== FIND TOPPER ====\n")

    if len(students) == 0:
        print("No Student Available")
        return
    
    highest = 0
    topper = None

    for student in students:
        if student["Marks"] > highest:
            highest = student["Marks"]
            topper = student

    print("ID: ", topper["ID"])
    print("Name: ", topper["Name"])
    print("Age: ", topper["Age"])
    print("Course: ", topper["Course"])
    print("Marks: ", topper["Marks"])

    print("\n==== TOPPER FOUND SUCCESSFULLY ====\n")        

def find_failed():
    print("\n==== FAILED STUDENTS ====\n")

    if len(students) == 0:
        print("No Student Available!")
        return
    
    found = False

    for student in students:
        if student["Marks"] < 40:
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])
            print("Marks:", student["Marks"])

            found = True

    if found == False:
        print("No Failed Students!")

    else:
        print("\n==== FAILED STUDENT FOUND SUCCESSFULLY! ====\n")


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

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        calc_avg()

    elif choice == "7":
        find_topper()

    elif choice == "8":
        find_failed()

    elif choice == "9":
        break

    else:
        print("Invalid choice!")