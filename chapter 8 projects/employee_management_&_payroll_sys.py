employees = []

def add_employee():
    print("\n==== ADD EMPLOYEE ====\n")

    try:
        emp_id = int(input("Enter Employee ID: "))

    except ValueError:
        print("Please Enter a Valid Employee ID!")
        return
    
    name = input("Enter Employee Name: ")

    try:
        age = int(input("Enter Employee's Age: "))

        if age < 0:
            print("Age Cannot be Negative!")
            return
        
    except ValueError:
        print("Please Enter a Valid Age!")
        return
    
    dep = input("Enter Employee Department: ")

    try:
        bas_sal = float(input("Enter Employee's Salary: "))

        if bas_sal < 0:
            print("Salary Cannot be Negative!")
            return

    except ValueError:
        print("Please Enter a Valid Salary!")
        return
    
    employee = {
        "ID": emp_id,
        "name": name,
        "age": age,
        "dep": dep,
        "bas_sal": bas_sal
    }

    employees.append(employee)

    print("\n==== EMPLOYEE ADDED SUCCESSFULLY ====\n")

def view_all_employee():
    print("\n==== VIEW ALL EMPLOYEES ====\n")

    if len(employees) == 0:
        print("No Employee Available!")

    else:
        for employee in employees:
            print("Employee's ID: ", employee["ID"])
            print("Employee's Name: ", employee["name"])
            print("Employee's Age: ", employee["age"])
            print("Employee's Department: ", employee["dep"])
            print("Employee's Salary: \n", employee["bas_sal"])

        print("\n==== EMPLOYEES PRINT SUCCESSFULLY ====\n")

def search_employee():
    print("\n==== SEARCH EMPLOYEE ====\n")

    emp_id = int(input("Enter Employee's ID to search: "))

    if len(employees) == 0:
        print("No Employees Available!")

    else:
        found = False
        for employee in employees:
            if(emp_id == employee["ID"]):
                print("Employee's ID: ", employee["ID"])
                print("Employee's Name: ", employee["name"])
                print("Employee's Age: ", employee["age"])
                print("Employee's Department: ", employee["dep"])
                print("Employee's Salary: ", employee["bas_sal"])

                found = True
                break

        if found == False:
            print("Employee Not Found!")

        else:
            print("\n==== EMPLOYEES PRINT SUCCESSFULLY ====\n")

def update_employee():
    print("\n==== UPDATE EMPLOYEE ====\n")

    emp_id = int(input("Enter Employee's ID to update: "))

    if len(employees) == 0:
        print("No Employees Available")

    else:
        found = False
        for employee in employees:
            if(emp_id == employee["ID"]):
                new_id = int(input("Enter New ID: "))
                new_name = input("Enter New Name: ")
                new_age = int(input("Enter New Age: "))
                new_dep = input("Enter New Department: ")
                new_bas_sal = float(input("Enter New Salary: "))

                employee["ID"] = new_id
                employee["name"] = new_name
                employee["age"] = new_age
                employee["dep"] = new_dep
                employee["bas_sal"] = new_bas_sal

                found = True
                break

        if found == False:
            print("Employee Not Found!")

        else:
            print("\n==== EMPLOYEE UPDATED SUCCESSFULLY ====\n")
            print("Employee's New ID: ", employee["ID"])
            print("Employee's New Name: ", employee["name"])
            print("Employee's New Age: ", employee["age"])
            print("Employee's New Department: ", employee["dep"])
            print("Employee's New Salary: ", employee["bas_sal"])


def delete_employee():
    print("\n==== DELETE EMPLOYEE ====\n")

    emp_id = int(input("Enter Employee's ID you want to Delete: "))

    if len(employees) == 0:
        print("No Employees Availabel!")

    else:
        found = False
        for employee in employees:
            if(emp_id == employee["ID"]):
                employees.remove(employee)

                found = True
                break

        if found == False:
            print("Employee Not Found")

        else:
            print("\n==== EMPLOYEE DELETED SUCCESSFULLY ====\n")

def calc_salary():
    print("\n==== CALCULATE SALARY ====\n")

    emp_id = int(input("Enter Employee's ID to Calculate Salary: "))

    if len(employees) == 0:
        print("No Employees Available!")

    else:
        found = False
        for employee in employees:
            if(emp_id == employee["ID"]):
                bonus = float(input("Enter Employee's Bonus: "))
                deduction = float(input("Enter Employee's Deduction: "))

                if(bonus < 0 or deduction < 0):
                    print("Please Enter Valid Entries!")

                else:
                    net_salary = employee["bas_sal"] + bonus - deduction
                    found = True
                    break

        if found == False:
            print("Employee Not Found!")

        else:
            print("\n==== SALARY CALCULATED SUCCESSFULLY ====\n")
            print("Employee's ID: ", employee["ID"])
            print("Employee's Name: ", employee["name"])
            print("Employee's Basic Salary: ", employee["bas_sal"])
            print("Employee's Bonus: ", bonus)
            print("Employee's Deduction: ", deduction)
            print("Employee's Net Salary: ", net_salary)

def high_paid_emp():
    print("\n==== HIGHEST PAID EMPLOYEE ====\n")

    if len(employees) == 0:
        print("No Employee Available!")
        return

    highest = 0
    rich = None

    for employee in employees:
        if employee["bas_sal"] > highest:
            highest = employee["bas_sal"]
            rich = employee

    print("\n==== HIGHEST PAID EMPLOYEE FOUND SUCCESSFULLY ====\n")
    print("Highest Salary's Employee ID:", rich["ID"])
    print("Highest Salary's Employee Name:", rich["name"])
    print("Highest Salary's Employee Age:", rich["age"])
    print("Highest Salary's Employee Department:", rich["dep"])
    print("Highest Salary's Employee Salary:", rich["bas_sal"])

def show_emp_by_dep():
    print("\n==== SHOW EMPLOYEE BY DEPARTMENT ====\n")

    emp_dep = input("Enter Department of the Employees: ")

    if len(employees) == 0:
        print("No Employee Available!")

    else:
        found = False

        for employee in employees:
            if emp_dep.lower() == employee["dep"].lower():

                print("Employee's ID:", employee["ID"])
                print("Employee's Name:", employee["name"])
                print("Employee's Age:", employee["age"])
                print("Employee's Department:", employee["dep"])
                print("Employee's Salary:", employee["bas_sal"])
                print()

                found = True

        if found == False:
            print("Employees Not Found!")

        else:
            print("\n==== EMPLOYEES FOUND SUCCESSFULLY ====\n")


while True:
    print("\n==== EMPLOYEE MANAGEMENT & PAYROLL SYSTMEM ====\n")

    print("1. Add Employee")
    print("2. View All Employee")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Calculate Salary")
    print("7. Find Highest Paid Employee")
    print("8. Show Employee by Department")
    print("9. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_all_employee()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        calc_salary()

    elif choice == "7":
        high_paid_emp()

    elif choice == "8":
        show_emp_by_dep()

    elif choice == "9":
        break