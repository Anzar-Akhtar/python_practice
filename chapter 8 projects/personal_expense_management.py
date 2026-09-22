expenses = []

while True:

    print("==== EXPENSE TRACKER ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Total Expense")
    print("5. Category-wise Expense")
    print("6. Highest Expense")
    print("7. Delete Expense")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if(choice == "8"):
        break

    elif(choice == "1"):
        print("==== Add Expense ====")
        expense_name = input("Enter Expense Name:")
        amt = float(input("Enter Amount:"))
        category = input("Enter Category:")
        date = input("Enter date:")

        expense = {
            "name": expense_name,
            "amount": amt,
            "category": category,
            "date": date
        }

        expenses.append(expense)
        print("Expense Added Successfully!")
        

    elif(choice == "2"):
        print("==== View All Expenses ====")

        for expense in expenses:
            print("Name: ", expense["name"])
            print("Amount: ", expense["amount"])
            print("Category: ", expense["category"])
            print("Date: ", expense["date"])

    elif(choice == "3"):
        print("==== Search Expense ====")

        # print(expenses)
        search_name = input("Enter Expense name to search: ")

        found = False
        for expense in expenses:
            if(search_name.lower() == expense["name"].lower()):
                print("Name: ", expense["name"])
                print("Amount: ", expense["amount"])
                print("Category: ", expense["category"])
                print("Date: ", expense["date"])

                found = True
            if found == False:
                print("Not Found")

    elif(choice == "4"):
        print("==== Total Expense ====")

        total = 0
        for expense in expenses:
            total = total + expense["amount"]

        print("Total Expense: ", total)

    elif(choice == "5"):
        print("==== Category-wise Expense ====")

        category_name = input("Enter Category: ")

        total = 0

        for expense in expenses:
            if(category_name.lower() == expense["category"].lower()):
                total = total + expense["amount"]

        print("Category Wise Expenses: ", total)

    elif(choice == "6"):
        print("==== Highest Expense ====")
        input("")

    elif(choice == "7"):
        print("==== Delete Expense ====")
        input("")

    else:
        print("Invalid Choice")
