balance = 10000

amount = int(input("Enter withdrawl amount: "))

if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient balance")
else:
    balance = balance - amount
    print("withdrawl Successful")
    print("Remaining Balance:", balance)
    