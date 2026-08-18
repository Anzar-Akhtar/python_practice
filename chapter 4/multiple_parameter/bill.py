def calc_bill(price, quantity):
    total = price * quantity
    print("Total bill amount:", total)


price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

calc_bill(price, quantity)