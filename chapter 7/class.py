class Employee:

    company = "Google"


    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {self.company}")


em1 = Employee("Anzar", 20000)
em2 = Employee("Atah", 22000)

em1.show_details()
print("\n")
em2.show_details()

Employee.change_company("Meta")
print(em1.company)
print(em2.company)




class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_schoolName(cls, new_school):
        cls.school = new_school


s1 = Student("Anzar")

print("\nBefore: ", s1.school)
Student.change_schoolName("XYZ School")
print("After: ", s1.school)



class Bank:

    bank_name = "SBI"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name


customer1 = Bank("Anzar")
customer2 = Bank("Atah")

print(customer1.bank_name)
print(customer2.bank_name)

Bank.change_bank_name("HDFC")

print(customer1.bank_name)
print(customer2.bank_name)
