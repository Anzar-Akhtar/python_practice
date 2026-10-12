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

def book_appointment():
    print("\n==== BOOK APPOINTMNET ====\n")

    if len(patients) == 0:
        print("No Patient Registered!!")
        return

    try:
        appointment_id = int(input("Enter Appointment ID: "))

    except ValueError:
        print("Please Enter the Valid Appointment ID!!")
        return

    for appointment in appointments:
        if(appointment_id == appointment["appointment_id"]):
            print("Appointment ID Already Exist!!")
            return

    try:
        patient_id = int(input("Enter Patient ID: "))

    except ValueError:
        print("Please Enter a Valid Patient ID!!")
        return

    patient_found = None
    for patient in patients:
        if patient_id == patient["ID"]:
            patient_found == patient
            break

    if patient_found is None:
        print("Patient Not Found! Please Register First!!")
        return

    appointment_date = input(
        "Enter Appointment Date (YYYY-MM-DD): "
    ).strip()

    if appointment_date == "":
        print("Appointment Date Cannot Be Empty!!")
        return

    appointment_time = input(
        "Enter Appointment Time (HH:MM): "
    ).strip()

    if appointment_time == "":
        print("Appointment Time Cannot Be Empty!!")
        return

    dr_name = patient_found["doctor"]

    for appointment in appointments:
        if(
            appointment["doctor"] == dr_name
            and appointment["date"] == appointment_date
            and appointment["time"] == appointment_time
        ):
            print("This Doctor's Time Slot Is Already Booked!")
            return

    appointment = {
        "appointment_id": appointment_id,
        "patient_id": patient_id,
        "doctor": dr_name,
        "date": appointment_date,
        "time": appointment_time
    }

    appointments.append(appointment)

    print("\n==== APPOINTMENT BOOKED SUCCESSFULLY ====\n")
    print("Appointment ID:", appointment_id)
    print("Patient ID:", patient_id)
    print("Patient Name:", patient_found["name"])
    print("Doctor Name:", dr_name)
    print("Appointment Date:", appointment_date)
    print("Appointment Time:", appointment_time)

def cancel_appointment():
    print("\n==== CANCEL APPOINTMNET ====\n")

    if len(appointments) == 0:
        print("No Appoitments Available!!")
        return

    try:
        cancel_id = int(input("Enter Appointment ID to Cancel: "))

    except ValueError:
        print("Please Enter a Valid Appointment ID!!")
        return

    found = False
    for appointment in appointments:
        if(cancel_id == appointment["appointment_id"]):
            appointments.remove(appointment)
            found = True
            break

    if not found:
        print("Appointment Not Found!!")
        return

    print("\n==== APPOINTMENT CANCELLED SUCCESSFULLY ====\n")

def generate_bill():
    print("\n==== GENERATE PATIENT BILL ====\n")

    if len(patients) == 0:
        print("No Patient Available!!")
        return

    try:
        bill_id = int(input("Enter Patient ID to Generate Bill: "))

    except ValueError:
        print("Please Enter a Valid ID")
        return

    found = False
    total_bill = 0
    for patient in patients:
        if(bill_id == patient["ID"]):
            print("Patient ID: ", patient["ID"])
            print("Patient Name: ", patient["name"])
            print("Dr. Name: ", patient["doctor"])
            print("Fees: ", patient["fee"])

            total_bill = patient["fee"]
            found = True
            break

    if not found:
        print("No Patient Found!!")
        return

    print("\nTotal Bill is: ", total_bill)
    print("\n==== BILL GENERATED SUCCESSFULLY ====\n")

def patient_by_dr():
    print("\n==== SHOW PATIENTS BY DOCTOR ====\n")

    if len(patients) == 0:
        print("No Patients Available!!")
        return

    try:
        dr_name = input("Enter Doctor Name: ").strip()

        if dr_name == "":
            print("Doctor Name Cannot Be Empty!!")
            return

        if dr_name.isdigit():
            print("Doctor Name Cannot Contain Only Numbers!!")
            return

    except ValueError:
        print("Please Enter a Valid Doctor Name!!!")
        return

    found = False
    for patient in patients:
        if(dr_name.islower() == patient["doctor"].islower()):

            print("Patient ID: ", patient["ID"])
            print("Patient Name: ", patient["name"])
            print("Patient Age: ", patient["age"])
            print("Patient gender: ", patient["gender"])
            print("Patient Desease: ", patient["disease"])
            print("Patient's Doctor Name: ", patient["doctor"])
            print("Patient's Doctor Fees: ", patient["fee"])

            found = True

    if not found:
        print("No Patient Found For This Doctor!!")
        return

    print("\n==== PATIENTS PRINTED SUCCESSFULLY ====\n")

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
        delete_patient()

    elif choice == "6":
        book_appointment()

    elif choice == "7":
        cancel_appointment()

    elif choice == "8":
        generate_bill()

    elif choice == "9":
        patient_by_dr()

    elif choice == "10":
        pass

    elif choice == "11":
        print("\n==== THANK YOU FOR USING HOSPITAL MANAGEMENT SYSTEM ====\n")
        break