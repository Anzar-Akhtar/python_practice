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

def view_all_products():
    print("\n==== VIEW ALL PRODUCTS ====\n")

    if len(products) == 0:
        print("No Products Available!")
        return

    else:
        for product in products:
            print("Product ID: ", product["ID"])
            print("Product Name: ", product["name"])
            print("Product Category: ", product["category"])
            print("Product Price: ", product["price"])
            print("Product Quantity: ", product["quantity"])

        print("\n==== PRODUCTS PRINTED  SUCCESSFULLY ====\n")
    
def search_product():
    print("\n==== SEARCH PRODUCTS ====\n")

    if len(products) == 0:
        print("No Products Available!")
        return
    
    try:
        search_id = int(input("Enter Product ID to Search: "))

    except ValueError:
        print("Please Enter the Valid Product ID!!")
        return

    found = False
    for product in products:
        if(search_id == product["ID"]):
            print("Product ID: ", product["ID"])
            print("Product Name: ", product["name"])
            print("Product Category: ", product["category"])
            print("Product Price: ", product["price"])
            print("Product Quantity: ", product["quantity"])

            found = True
            break

    if found == False:
        print("Product Not found!")
        return

    else:
        print("\n==== PRODUCT SEARCHED SUCCESSFULLY ====\n")

def update_product():
    print("\n==== UPDATE PRODUCT ====\n")

    if len(products) == 0:
        print("No Product Available")
        return

    try:
        update_id = int(input("Enter the Product ID you wants to Update: "))

    except ValueError:
        print("Please Enter the Valid Product ID")
        return

    found = False
    for product in products:
        if(update_id == product["ID"]):
            try:
                new_id = int(input("Enter the new ID: "))

            except ValueError:
                print("Please Enter the Valid ID")
                return

            for p in products:
                if(new_id == p["ID"] and product["ID"] != new_id):
                    print("ID Already Exists!")
                    return

            new_name = input("Enter the new Name: ")

            if new_name == "":
                print("Name Cannot Be Empty!")
                return

            if new_name.isdigit():
                print("Name Cannot Contain Only Numbers")
                return

            new_cat = input("Enter new Category:")

            if new_cat == "":
                print("Category Cannot Be Empty!")
                return

            if new_cat.isdigit():
                print("Category Cannot Cantain Only Number")
                return

            try:
                new_price = int(input("Enter the new Proce: "))

                if new_price < 0:
                    print("Price Cannot Be Negative!")
                    return

            except ValueError:
                print("Please Enter the Valid Price!!")
                return

            try:
                new_quan = int(input("Enter the new Quantity: "))

                if new_quan < 0:
                    print("Quantity Cannot Be Negative!")
                    return

            except ValueError:
                print("Please Enter the Valid Quantity")
                return

            product["ID"] = new_id
            product["name"] = new_name
            product["category"] = new_cat
            product["price"] = new_price
            product["quantity"] = new_quan

            found = True
            break

    if found == False:
        print("Product Not found!!")
        return

    else:
        print("\n==== PRODUCT UPDATED SUCCESSFULLY ====\n")
        print("Product New ID: ", product["ID"])
        print("Product New Name: ", product["name"])
        print("Product New Category: ", product["category"])
        print("Product New Price: ", product["price"])
        print("Product New Quantity: ", product["quantity"])
            
def del_product():
    print("\n==== DELETE PRODUCT ====\n")

    if len(products) == 0:
        print("No Product Available!!")
        return

    try:
        dlt_id = int(input("Enter the Product ID you want Delete: "))

    except ValueError:
        print("Please Enter the Valid Product ID!!")
        return

    found = False
    for product in products:
        if(dlt_id == product["ID"]):
            products.remove(product)

            found = True
            break

    if found == False:
        print("Product Not Found!")
        return

    else:
        print("\n==== PRODUCT DELETED SUCCESSFULLY! ====\n")



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
        view_all_products()

    if choice == "3":
        search_product()

    if choice == "4":
        update_product()

    if choice == "5":
        del_product()

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