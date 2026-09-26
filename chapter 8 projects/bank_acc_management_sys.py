accounts = []

def create_acc():
    print("\n==== CREATE ACCOUNT ====\n")

    acc_no = int(input("Enter Your Account No.: "))
    name = input("Enter Your Name: ")
    age = int(input("Enter Your Age: "))
    acc_type = input("Enter Account Type: ")
    balance = float(input("Enter Balance: "))

    account = {
        "acc_no": acc_no,
        "name": name,
        "age": age,
        "acc_type": acc_type,
        "balance": balance
    }

    accounts.append(account)
    print("\n==== ACCOUNT ADDED SUCCESSFULLY ====\n")


def view_all_acc():
    print("\n==== VIEW ALL ACCOUNTS ====\n")

    if len(accounts) == 0:
        print("No Accounts Available!")

    else:
        for account in accounts:
            print("Account NO: ", account["acc_no"])
            print("Name: ", account["name"])
            print("Age: ", account["age"])
            print("Account Tyoe: ", account["acc_type"])
            print("Balance: ", account["balance"])

def search_acc():
    print("\n==== SEARCH YOUR ACCOUNT ====\n")

    search_acc_no = int(input("Enter Your Account No.: "))

    if len(accounts) == 0:
        print("No Accounts Available!")

    else:
        found = False
        for account in accounts:
            if (search_acc_no == account["acc_no"]):
                print("Account NO: ", account["acc_no"])
                print("Name: ", account["name"])
                print("Age: ", account["age"])
                print("Account Type: ", account["acc_type"])
                print("Balance: ", account["balance"])

                print("\n==== ACCOUNT FOUND SUCCESSFULLY ====\n")
                found = True
        if found == False:
            print("Account Not Found!")

def deposit_money():
    print("\n==== DEPOSIT MONEY ====\n")

    acc_no = int(input("Enter Your Account No. to Deposit Money: "))

    if len(accounts) == 0:
        print("No Account Available!")

    else:
        found = False
        for account in accounts:
            if(acc_no == account["acc_no"]):
                mon_dep = float(input("Enter Money to Deposit: "))

                if mon_dep == 0:
                    print("Deposit Money can't be zero")

                elif mon_dep < 0:
                    print("Deposit Money can't be negative")

                else:
                    account["balance"] += mon_dep
                    print("\n==== BALANCE UPDATED ====\n")
                found = True

        if found == False:
            print("Account Not found!")

def withdrawl_money():
    print("\n==== WITHDRAWL MONEY ====\n")

    acc_no = int(input("Enter Your Account No. to Withdrawl Money: "))

    if len(accounts) == 0:
        print("No Account Available!")

    else:
        found = False
        for account in accounts:
            if(acc_no == account["acc_no"]):
                with_mon = float(input("Enter the Amount you wants to Withdrawl: "))

                if with_mon == 0:
                    print("Withdrawl Money can't be zero!")

                elif with_mon < 0:
                    print("Withdrawl Money can't be Negative")

                elif with_mon > account["balance"]:
                    print("Insufficient Balance! Please Enter Valid Money")

                else:
                    account["balance"] -= with_mon
                    print("\n==== AMOUNT WITHDRAWL ====\n")
                found = True

        if found == False:
            print("Account Not Found!")

def check_bal():
    print("\n==== CHECK BALANCE ====\n")

    search_bal = int(input("Enter Your Account No. to check Balance: "))

    if len(accounts) == 0:
        print("No Account Available!")

    else:
        found = False
        for account in accounts:
            if(search_bal == account["acc_no"]):
                print("Your Account Balance is: ", account["balance"])
                found = True

        if found == False:
            print("Account Not found!")

def update_acc():
    print("\n==== UPDATE MONEY ====\n")

    acc_no = int(input("Enter Your Account No. to Update Account: "))

    if len(accounts) == 0:
        print("No Account Available!")

    else:
        found = False
        for account in accounts:
            if(acc_no == account["acc_no"]):
                new_name = input("Enter Your New Name: ")
                new_age = int(input("Enter Your New Age: "))
                new_acc_type = input("Enter Your New Account Type: ")


                account["name"] = new_name
                account["age"] = new_age
                account["acc_type"] = new_acc_type


                print("\n==== ACCOUNT UPDATED SUCCESSFULLY ====\n")

                print("Account No.:", account["acc_no"])
                print("Updated Name:", account["name"])
                print("Updated Age:", account["age"])
                print("Updated Account Type:", account["acc_type"])
                print("Balance:", account["balance"])

                found = True

        if found == False:
            print("Account Not found!")

def delete_acc():
    print("\n==== DELETE ACCOUNT ====\n")

    if len(accounts) == 0:
        print("No Accounts Available!")

    else:
        found = False
        acc_no = int(input('Enter Your Account No. to Delete Your Account: '))

        for account in accounts:
            if(acc_no == account["acc_no"]):

                accounts.remove(account)
                found = True

                print("\n==== ACCOUNT DELETED SUCCESSFULLY! ====\n")

        if found == False:
            print("Account Not Found!")

while True:
    print("\n==== BANK ACCOUNT MANAGEMENT SYSTEM ====\n")

    print("1. Create Account")
    print("2. View All Account")
    print("3. Search Account")
    print("4. Deposit Money")
    print("5. Withdrawl Money")
    print("6. Check Balance")
    print("7. Update Account")
    print("8. Delete Account")
    print("9. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        create_acc()

    elif choice == "2":
        view_all_acc()

    elif choice == "3":
        search_acc()

    elif choice == "4":
        deposit_money()

    elif choice == "5":
        withdrawl_money()

    elif choice == "6":
        check_bal()

    elif choice == "7":
        update_acc()

    elif choice == "8":
        delete_acc()

    elif choice == "9":
        break