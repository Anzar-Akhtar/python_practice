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
        pass

    elif choice == "3":
        pass

    elif choice == "4":
        pass

    elif choice == "5":
        pass

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

