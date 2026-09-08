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




class College:

    college_name = "TMU"

    def __init__ (self, student_name, course):
        self.college_name = student_name
        self.course = course

    @classmethod
    def change_college(cls, new_college):
        cls.college_name = new_college


s1 = College("Anzar", "BCA")
s2 = College("Atah", "B.Com")

print(s1.college_name)
print(s2.college_name)
print("\n")

College.change_college("ABC")
print(s1.college_name)
print(s2.college_name)



class Product:

    store_name = "Amazon"

    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def show_product(self):
        print(f"Name: {self.product_name}")
        print(f"Price: {self.price}")
        print(f"Store: {self.store_name}")

    @classmethod
    def change_store(cls, new_store):
        cls.store_name = new_store

p1 = Product("Laptop", 50000)
p2 = Product("Mobile", 20000)

p1.show_product()
print("\n")
p2.show_product()

print("\nChanging store name...\n")
print("Before: ", Product.store_name)

Product.change_store("Flipkart")

print("After: ", Product.store_name)
print("\n")

p1.show_product()
print("\n")
p2.show_product()