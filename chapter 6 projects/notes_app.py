while True:

    print("\n===== NOTES APP =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        note = input("Enter your note: ")

        with open("note.txt", "a") as file:
            file.write(note + "\n")

        print("Note Saved Successfully!")
        break

    elif choice == "2":
        try:
            with open("note.txt", "r") as file:
                notes = file.read()

            print("\n==== YOUR NOTES =====")
            print(notes)
            break

        except FileNotFoundError:
            print("No Notes found!")

    elif choice == "3":
        print("GoodBye, Thank You!")
        break

    else:
        print("Invalid choice!")