expenses = []

while True:

    print("==== EXPENSE TRACKER ====\n")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Total Expense")
    print("5. Category-wise Expense")
    print("6. Highest Expense")
    print("7. Delete Expense")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    def add_expense():

        print("\n==== Add Expense ====\n")
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

    def view_expense():
        print("\n==== View All Expenses ====\n")
        
        if len(expenses) == 0:
            print("No expense available!")

        else:
            for expense in expenses:
                print("Name: ", expense["name"])
                print("Amount: ", expense["amount"])
                print("Category: ", expense["category"])
                print("Date: ", expense["date"])

    def search_expense():
        print("\n==== Search Expense ====\n")
        
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
        
    def total_expense():
        print("\n==== Total Expense ====\n")
        
        total = 0
        for expense in expenses:
            total = total + expense["amount"]

        print("Total Expense: ", total)

    def category_wise_expense():
        print("\n==== Category-wise Expense ====\n")
        
        category_name = input("Enter Category: ")

        total = 0

        for expense in expenses:
            if(category_name.lower() == expense["category"].lower()):
                total = total + expense["amount"]

        print("Category Wise Expenses: ", total)

    def highest_expense():
        print("\n==== Highest Expense ====\n")
        
        if len(expenses) == 0:
            print("No expenses available!")

        else:
            highest = 0
            highest_expense = None
    
            for expense in expenses:
                if expense["amount"] > highest:
                    highest = expense["amount"]
                    highest_expense = expense
                    
            print("Highest Expense: ", highest)
            print("Name:", highest_expense["name"])
            print("Amount:", highest_expense["amount"])
            print("Category:", highest_expense["category"])
            print("Date:", highest_expense["date"])
                
    def delete_expense():
        print("\n==== Delete Expense ====\n")
        
        del_expense = input("Enter the expense you want to delete:")

        found = False
        for expense in expenses:
            if(del_expense.lower() == expense["name"].lower()):
                expenses.remove(expense)

                found = True
                print("\nExpense Deleted Successfully!\n")

        if found == False:
                print("Expense Not Found!")


    if(choice == "1"):
        add_expense()
        
    elif(choice == "2"):
        view_expense()   

    elif(choice == "3"):
       search_expense()

    elif(choice == "4"):
        total_expense()

    elif(choice == "5"):
        category_wise_expense()

    elif(choice == "6"):
        highest_expense()

    elif(choice == "7"):
        delete_expense()
        
    elif(choice == "8"):
        break

    else:
        print("Invalid Choice")
