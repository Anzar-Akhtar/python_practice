from datetime import datetime, timedelta
books = []
members = []
issued_books = []

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
        print("Book Title: ", book["title"])
        print("Book Author: ", book["author"])
        print("Book Quantity: ", book["quantity"])

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

def reg_member():
    print("\n==== REGISTER MEMBER ====\n")

    try:
        mem_id = int(input("Enter Member ID: "))

        if mem_id <= 0:
            print("Member ID Cannot Be Negative!!")
            return

    except ValueError:
        print("Please Enter Valid ID!!")
        return

    for m in members:
        if(mem_id == m["ID"]):
            print("ID Already Exist!!")
            return

    mem_name = input("Enter Member Name: ")

    if mem_name.strip() == "":
        print("Name Cannot Be Empty!!")
        return

    if mem_name.isdigit():
        print("Name Cannot Contain Only Numbers!!")
        return

    mem_no = input("Enter Your Contact Number: ")

    if mem_no.strip() == "":
        print("Contact Number Cannot Be Empty!!")
        return

    if not mem_no.isdigit() or len(mem_no) != 10:
        print("Please Enter a Valid 10-Digit Contact Number!!")
        return

    member = {
        "ID": mem_id,
        "name": mem_name,
        "contact": mem_no
    }
    members.append(member)
    print("\n==== MEMBER REGISTERED SUCCESSFULLY ====\n")

def issue_book():
    print("\n==== ISSUE BOOK ====\n")

    if len(books) == 0:
        print("No Book Available!!")
        return

    if len(members) == 0:
        print("No Member Registered!!")
        return

    try:
        book_id = int(input("Enter Book ID: "))

        if book_id <= 0:
            print("Book ID Must Be Positive!!")
            return

    except ValueError:
        print("Please Enter a Valid ID!!")
        return

    found = False
    for book in books:
        if(book_id == book["ID"]):
            found = True
            break
    if not found:
        print("Book Not Found!!")
        return
           
    if(book["quantity"] <= 0):
        print("Book Not Available!!")
        return
    
    try:
        mem_id = int(input("Enter Member ID: "))

        if mem_id <= 0:
            print("Member ID Must Be Positive!!")
            return

    except ValueError:
        print("Please Enter Valid ID!!")
        return

    mem_found = False
    for member in members:
        if(mem_id == member["ID"]):
            mem_found = True
            break

    if not mem_found:
        print("Member Not found!!")
        return

    issue_date = datetime.now().date()
    due_date = issue_date + timedelta(days=14)

    issue_record = {
        "book_id": book_id,
        "member_id": mem_id,
        "issue_date": issue_date.isoformat(),
        "due_date": due_date.isoformat()
    }

    issued_book.append(issue_record)

    book["quantity"] -= 1

    print("\n==== BOOK ISSUED SUCCESSFULLY ====")
    print("Book ID:", book_id)
    print("Member ID:", mem_id)
    print("Issue Date:", issue_date)
    print("Due Date:", due_date)
    print("Available Quantity:", book["quantity"])
    print()

def return_book():
    print("\n==== RETURN BOOK ====\n")

    if len(issued_books) == 0:
        print("No Books Have Been Issued!")
        return

    try:
        book_id = int(input("Enter Book ID: "))

    except ValueError:
        print("Please Enter a Valid Book ID!!")
        return

    try:
        mem_id = int(input("Enter Member ID: "))

    except ValueError:
        print("Please Enter a Valid Member ID!!")
        return

    found = False
    for record in issued_books:
        if record["book_id"] == book_id and record["member_id"] == mem_id:
            found = True
            break

    if not Found:
        print("Issue Record Not Found!!")
        print("Please Check Book ID and Member ID.")
        return

    for book in books:
        if book["ID"] == book_id:
            book["quantity"] += 1
            break

    issued_books.remove(record)

    print("\n==== BOOK RETURNED SUCCESSFULLY ====")
    print("Book ID: ", book_id)
    print("Member ID: ", mem_id)
    print("Available Quantity: ", book["quantity"])
    print()

def show_available_books():
    print("\n==== SHOW AVAILABLE BOOKS ====\n")

    if len(books) == 0:
        print("No Books Available!!")
        return

    found = False
    for book in books:
        if book["quantity"] > 0:
            print("Book ID:", book["ID"])
            print("Book Title:", book["title"])
            print("Book Author:", book["author"])
            print("Available Quantity:", book["quantity"])
            print()

            found = True

    if not found:
        print("No Book Currently Available!!")
        return

    print("\n==== AVAILABLE BOOK DISPLAYED SUCCESSFULLY ====\n")

def show_overdue_books():
    print("\n==== OVERDUE BOOKS ====\n")

    if len(issued_books) == 0:
        print("No Books Are Currently Available!!")
        return

    today = datetime.now().date()

    found = False
    for record in issued_books:
        due_date = datetime.strptime(
            record["due_date"], "%Y-%m-%d"
        ).date()

        if today > due_date:
            found = True

            print("Book_ID:", record["book_id"])
            print("Member ID:", record["member_id"])
            print("Issued Date:", record["issue_date"])
            print("Due Date:", record["due_date"])
            print("Days Overdue:", (today - due_date).days)
            print()

    if not found:
        print("No Overdue Books Found!!")
        return

    print("\n==== OVERDUE BOOKS DISPLAYED SUCCESSFULLY ====\n")


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
        reg_member()

    elif choice == "7":
        issue_book()

    elif choice == "8":
        return_book()

    elif choice == "9":
        show_available_books()

    elif choice == "10":
        show_overdue_books()

    elif choice == "11":
        pass

    elif choice == "12":
        pass

    elif choice == "13":
        print("\n==== THANK YOU FOR USING LIBRARY MANAGEMENT SYSTEM ====\n")
        break

