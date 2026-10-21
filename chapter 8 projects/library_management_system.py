books = []

def add_book():
    print("\n==== ADD BOOK ====\n")

    try:
        book_id = int(input("Enter Book ID: "))

    except ValueError:
        print("Please Enter the Valid ID")
        return
    
    for b in books:
        if(book_id == b["ID"]):
            print("ID Already Exists!")
            return


    book_title = input("Enter Book Title: ")

    if book_title.strip() == "":
        print("Book Title Cannot Be Empty!!")
        return

    if book_title.isdigit():
        print("Book Title Cannot Contain Only Numbers")
        return

    book_author = input("Enter Book Author: ")

    if book_author.strip() == "":
        print("Author Cannot Be Empty!!")
        return

    if book_author.isdigit():
        print("Book Author Cannot Contain Only Number!!")
        return

    try:
        book_quan = int(input("Enter Book Qantity: "))

        if book_quan < 0:
            print("Book Quantity Cannot Be Negative!!")
            return

    except ValueError:
        print("Please Enter Valid Quantity!!")
        return

    book = {
        "ID": book_id,
        "title": book_title,
        "author": book_author,
        "quantity": book_quan
    }
    books.append(book)
    print("\n==== BOOK ADDED SUCCESSFULLY ====\n")

def view_all_books():
    print("\n==== VIEW ALL BOOKS ====\n")

    if len(books) == 0:
        print("No Books Available!!")
        return

    for book in books:
        print("Book ID: ", book["ID"])
        print("Book TItle: ", book["title"])
        print("Book Author: ", book["author"])
        print("Book Title: ", book["title"])

    print("\n==== BOOKS PRINTED SUCCESSFULLY ====\n")

def search_book():
    print("\n==== SEARCH BOOK ====\n")

    if len(books) == 0:
        print("No Books Available!!")
        return

    try:
        search_id = int(input("Enter the Book ID to Search: "))

    except ValueError:
        print("Please Enter Valid ID!!")
        return
    
    found = False
    for book in books:
        if(search_id == book["ID"]):
            print("Book ID: ", book["ID"])
            print("Book TItle: ", book["title"])
            print("Book Author: ", book["author"])
            print("Book Title: ", book["title"])

            found = True
            break

    if found == False:
        print("Book Not Found!!")
        return

    else:
        print("\n==== BOOK FOUNDED SUCCESSFULLY ====\n")

def update_book():
    print("\n==== UPDATE BOOK ====\n")

    if len(books) == 0:
        print("No Book Available!!")
        return

    try:
        update_id = int(input("Enter The ID you wants to Update: "))

    except ValueError:
        print("Please Enter Valid ID!!")
        return

    found = False
    for book in books:
        if(update_id == book["ID"]):
            try:
                new_id = int(input("Enter Book ID: "))
        
            except ValueError:
                print("Please Enter the Valid ID")
                return
            
            for b in books:
                if(new_id == b["ID"]):
                    print("ID Already Exists!")
                    return

            new_title = input("Enter New Title: ")

            if new_title.strip() == "":
                print("Title Cannot Be Empty!!")
                return

            if new_title.isdigit():
                print("Name Cannot Contain Only Numbers!!")
                return

            new_author = input("Enter New Author: ")

            if new_author.strip() == "":
                print("Author Cannot Be Empty!!")
                return

            if new_author.isdigit():
                print("Author Name Cannot Contain Only Numbers!!")
                return

            try:
                new_quan = int(input("Enter New Quantity: "))

                if new_quan < 0 :
                    print("Quantity Cannot Be Negative!!")
                    return

            except ValueError:
                print("Please Enter Valid Quantity!!")
                return

            book["ID"] = new_id
            book["title"] = new_title
            book["author"] = new_author
            book["quantity"] = new_quan

            found = True
            break

    if found == False:
        print("Book Not Found!!")
        return

    else:
        print("\n==== BOOK UPDATED SUCCESSFULLY ====\n")

def delete_book():
    print("\n==== DELETE BOOK ====\n")

    if len(books) == 0:
        print("No Books Available!!")
        return

    try:
        dlt_id = int(input("Enter the ID you want to Delete: "))

    except ValueError:
        print("Please Enter Valid ID!!")
        return

    found = False
    for book in books:
        if(dlt_id == book["ID"]):
            books.remove(book)
            found = True
            break

    if found == False:
        print("Book Not Found!!")
        return

    else:
        print("\n==== BOOK DELETED SUCCESSFULLY ====\n")

while True:
    print("\n==== LIBRARY MANAGEMENT SYSTEM ====\n")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Register Member")
    print("7. Issue Book")
    print("8. Return Book")
    print("9. Show Availble Books")
    print("10. Show Overdue Books")
    print("11. Calculate Fine")
    print("12. Save and Load Data from File")
    print("13. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_all_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        update_book()

    elif choice == "5":
        delete_book()

    elif choice == "6":
        pass

    elif choice == "7":
        pass

    elif choice == "8":
        pass

    elif choice == "9":
        pass

    elif choice == "10":
        pass

    elif choice == "11":
        pass

    elif choice == "12":
        pass

    elif choice == "13":
        print("\n==== THANK YOU FOR USING LIBRARY MANAGEMENT SYSTEM ====\n")
        break

