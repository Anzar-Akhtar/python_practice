patients = []
appointments = []

def add_patient():
    print("\n==== ADD PATIENT ====\n")

    try:
        patient_id = int(input("Enter Patient ID: "))

    except ValueError:
        print("Please Enter the valid ID")
        return

    for patient in patients:
        if(patient_id == patient["ID"]):
            print("Patient ID already exist!")
            return
        
    try:
        patient_name = input("Enter Patient Name: ")

        if patient_name == "":
            print("Name Cannot Be Empty!")
            return

        if patient_name.isdigit():
            print("Name Cannot Contain Only Number")
            return

    except ValueError:
        print("Please Enter the Valid Name!")
        return

    try:
        patient_age = int(input("Enter Patient Age: "))

        if patient_age <= 0:
            print("Age Cannot Be Negative!")
            return

        if patient_age == "":
            print("Patient Cannot Be Empty!")
            return

    except ValueError:
        print("Please Enter the Valid Age!")
        return

    try:
        patient_gender = input("Enter the Gender of the Patient: ")

        if patient_gender == "":
            print("Gender Cannot Be Empty")
            return

        if patient_gender.isdigit():
            print("Gender Cannot Be Number!!")
            return

    except ValueError:
        print("Please Enter the Valid Gender")
        return

    try:
        patient_des = input("Enter the Patient Desease: ")

        if patient_des == "":
            print("Desease Cannot Be Empty!")
            return

        if patient_des.isdigit():
            print("Desease Cannot Be Number!")
            return

    except ValueError:
        print("Please Enter the Valid Desease!!")
        return

    try:
        dr_name = input("Enter the Dr. Name: ")

        if dr_name == "":
            print("Name Cannot Be Empty!")
            return

        if dr_name.isdigit():
            print("Dr. Name Cannot Be Number!")
            return

    except ValueError:
        print("Please Enter the Valid DR. Name!!")
        return

    try:
        fees = float(input("Enter the Fee of the Dr. : "))

        if fees <= 0:
            print("Fee Cannot Be Negative!!")
            return

        if fees == "":
            print("Fees Cannot Be Empty")
            return

    except ValueError:
        print("Please Enter the Valid Fees!!")
        return

    patient = {
        "ID": patient_id,
        "name": patient_name,
        "age": patient_age,
        "gender": patient_gender,
        "disease": patient_des,
        "doctor": dr_name,
        "fee": fees
    }
    patients.append(patient)

    print("\n==== PATIENT ADDED SUCCESSFULY ====\n")
    

while True:
    print("\n==== HOSPITAL MANAGEMENT SYSTEM ====\n")
    print("1. Add Patient")
    print("2. View All Patient")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Book Appointment")
    print("7. Cancel Appointment")
    print("8. Generate Patient Bill")
    print("9. Show Patients By Doctor")
    print("10. Show Total Revenue")
    print("11. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_patient()

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
        print("\n==== THANK YOU FOR USING HOSPITAL MANAGEMENT SYSTEM ====\n")
        break
    