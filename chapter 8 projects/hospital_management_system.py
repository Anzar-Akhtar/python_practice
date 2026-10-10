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
    
def view_all_patient():
    print("\n==== VIEW ALL PATIENT ====\n")

    if len(patients) == 0:
        print("No Patients Available!")
        return

    else:
        for patient in patients:
            print("Patient ID: ", patient["ID"])
            print("Patient Name: ", patient["name"])
            print("Patient Age: ", patient["age"])
            print("Patient gender: ", patient["gender"])
            print("Patient Desease: ", patient["disease"])
            print("Patient's Doctor Name: ", patient["doctor"])
            print("Patient's Doctor Fees: ", patient["fee"])

        print("\n==== PATIENTS PRINTED SUCCESSFULLY ====\n")

def search_patient():
    print("\n==== SEARCH PATIENT ====\n")

    if len(patients) == 0:
        print("No Patient Available!")
        return

    try:
        search_id = int(input("Enter Patient ID: "))

    except ValueError:
        print("Please Enter the Valid Patient ID!")
        return

    found = False
    for patient in patients:
        if(search_id == patient["ID"]):
            print("Patient ID: ", patient["ID"])
            print("Patient Name: ", patient["name"])
            print("Patient Age: ", patient["age"])
            print("Patient gender: ", patient["gender"])
            print("Patient Desease: ", patient["disease"])
            print("Patient's Doctor Name: ", patient["doctor"])
            print("Patient's Doctor Fees: ", patient["fee"])

            found = True
            break

    if found == False:
        print("Patient Not Found!!")
        return

    else:
        print("\n==== PATIENT FOUNDED SUCCESSFULLY ====\n")

def update_patient():
    print("\n==== UPDATE PATEINT ====\n")

    if len(patients) == 0:
        print("No Patient Available!!")
        return

    try:
        update_id = int(input("Enter the Pateint ID to Update: "))

    except ValueError:
        print("Please Enter the Valid Patient ID!!")
        return

    found = False
    for patient in patients:
        if(update_id == patient["ID"]):
            try:
                new_id = int(input("Enter the New Patient ID: "))

            except ValueError:
                print("Please Enter the Valid ID!!")
                return

            for p in patients:
                if(new_id == p["ID"] and patient["ID"] != new_id):
                    print("ID Already Exists!")
                    return

            new_name = input("Enter the New Patient Name: ")

            if new_name == "":
                print("Name Cannot Be Empty!")
                return

            if new_name.isdigit():
                print("Name Cannot Contain Only Numbers!!")
                return

            try:
                new_age = int(input("Enter the New Patient Age: "))

                if new_age <= 0:
                    print("Age Must Be Positive!")
                    return

            except ValueError:
                print("Please Enter the Valid Age!!")
                return

            try:
                new_gen = input("Enter the New Gender: ")

                if new_gen == "":
                    print("Gender Cannot Be Empty!!")
                    return

                if new_gen.isdigit():
                    print("Gender Cannot Contain Number!!")
                    return

            except ValueError:
                print("Please Enter the Valid Gender!!")
                return

            try:
                new_des = input("Enter the New Desease: ")

                if new_des == "":
                    print("Disease Cannot Be Empty!!")
                    return

                if new_des.isdigit():
                    print("Disease Cannot Contain Numbers!!")
                    return

            except ValueError:
                print("Please Enter the Valid Disease")
                return

            try:
                new_dr = input("Enter the New Dr. Name: ")

                if new_dr == "":
                    print("Dr. Name Cannot Be Empty!!")
                    return

                if new_dr.isdigit():
                    print("Dr. Name Cannot Contain only Numbers")
                    return

            except ValueError:
                print("Please Enter the Valid Dr. Name")
                return

            try:
                new_fee = float(input("Enter the New Dr. fees: "))

                if new_fee <= 0:
                    print("Fees Must Be Postive!!")
                    return

            except ValueError:
                print("Please Enter the Valid Fees!!")
                return

            patient["ID"] = new_id
            patient["name"] = new_name
            patient["age"] = new_age
            patient["gender"] = new_gen
            patient["disease"] = new_des
            patient["doctor"] = new_dr
            patient["fee"] = new_fee

            found = True
            break

    if found == False:
        print("Patient Not Found!!")
        return

    print("\n==== PATIENT UPDATED SUCCESSFULLY ====\n")

def delete_patient():
    print("\n==== DELETE PATIENT ====\n")

    if len(patients) == 0:
        print("No Patient Available!")
        return
    
    try:
        dlt_id = int(input("Enter The Patient ID you want to Delete: "))

    except ValueError:
        print("Please Enter The Valid ID!!")
        return
    
    found = False
    for patient in patients:
        if(dlt_id == patient["ID"]):
            patients.remove(patient)
            found = True
            break

    if found == False:
        print("Patient Not Found!!")
        return

    print("\n==== PATIENT DELETED SUCCESSFULLY ====\n")

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
        view_all_patient()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        update_patient()

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
    