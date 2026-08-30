while True:

    print("\n==== STUDENT MANAGER ====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")

        with open("dairy.txt", "a") as file:
            file.write(name + "\n")

        print("Student added successfully!!")
        break

    elif choice == "2":

        try:
            with open("dairy.txt", "r") as file:
                students = file.read().splitlines()

            if len(students) == 0:
                print("No Student found!")
            else:
                print("n==== STUDENTS ====")

                for student in students:
                    print(student)

        except FileNotFoundError:
            print("Student file does not exist!")


    elif choice == "3":

        search = input("Enter student name: ")

        try:
            with open("dairy.txt", "r") as file:
                students = file.read().splitlines()

            if search in students:
                print("Student Found!")
            else:
                print("Student not found!!")

        except FileNotFoundError:
            print("Student file does not exist!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")