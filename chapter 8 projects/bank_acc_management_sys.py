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
    print(accounts)

def view_all_acc():
    pass

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

    if choice == "9":
        break