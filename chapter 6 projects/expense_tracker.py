while True:

    print("\n ==== EXPENSE TRACKER ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        with open("expense.txt", "a") as file:
            file.write(name + "|" + str(amount) + "\n")

        print("Expense added successfully!!")

    elif choice == "2":

        try:
            with open("expense.txt", "r") as file:
                expenses = file.read().splitlines()

            print("\n ==== EXPENSES ====")

            for expense in expenses:
                data = expense.split("|")

                print("Name:", data[0])
                print("Amount:", data[1])
                print()

        except FileNotFoundError:
            print("No expenses found!")


    elif choice == "3":

        total = 0

        try:
            with open("expense.txt", "r") as file:
                expenses = file.read().splitlines()

                for expense in expenses:
                    data = expense.split("|")
                    total += float(data[1])

                print("Total Expenses:", total)

        except FileNotFoundError:
            print("No expenses found!")


    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")