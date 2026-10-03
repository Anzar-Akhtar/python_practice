products = []

def add_products():
    print("\n==== ADD PRODUCTS ====\n")

    try:
        pro_id = int(input("Enter Product ID: "))

    except ValueError:
        print("Please Enter a Valid Product ID!")
        return

    for product in products:
        if(pro_id == product["ID"]):
            print("Product ID Already Exists!")
            return

    try:
        pro_name = input("Enter Product Name: ")

        if pro_name == "":
            print("Name Cannot Be Empty!")
            return

        if pro_name.isdigit():
            print("Product Name Cannot Contain Only Number!")
            return

    except ValueError:
        print("Please Enter a Valid Name!")
        return

    try:
        pro_cat = input("Enter Product Category: ")

        if pro_cat == "":
            print("Product Category Cannot Be Empty!")
            return

        if pro_cat.isdigit():
            print("Product Category Cannot Cantain Only Numbers")
            return

    except ValueError:
        print("Please Enter a Valid Product Category!")
        return

    try:
        pro_price = float(input("Enter Product Price: "))

        if pro_price < 0:
            print("Product Price Cannot Be Negative!")
            return

    except ValueError:
        print("Please Enter a Valid Product Price!")
        return

    try:
        pro_quan = int(input("Enter Product Quantity: "))

        if pro_quan < 0:
            print("Product Quantity Cannot Be Negative!")
            return

    except ValueError:
        print("Please Enter a Valid Product Quantity!")
        return

    product = {
        "ID": pro_id,
        "name": pro_name,
        "category": pro_cat,
        "price": pro_price,
        "quantity": pro_quan
    }
    products.append(product)

    print("\n==== PRODUCT ADDED SUCCESSFULLY ====\n")

while True:
    print("==== INVENTORY MANAGEMENT SYSTEM ====")
    print("1. Add Product")
    print("2. View All Products")
    print("3. Search Products")
    print("4. Update Products")
    print("5. Delete Products")
    print("6. Sell Products")
    print("7. Restock Products")
    print("8. Show Low Stock Products")
    print("9. Calculate Total Inventory Value")
    print("10. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_products()

    if choice == "2":
        pass

    if choice == "3":
        pass

    if choice == "4":
        pass

    if choice == "5":
        pass

    if choice == "6":
        pass

    if choice == "7":
        pass

    if choice == "8":
        pass

    if choice == "9":
        pass

    if choice == "10":
        print("\n==== THANK YOU FOR USING INVENTORY MANAGEMENT SYSTEM! ====")
        break

    else:
        print("Invalid Choice")