class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


result = Calculator.add(5, 3)
print(result)


class Student:

    school = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"School: {self.school}")

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    @staticmethod
    def welcome():
        print("Welcome to the new school!")


s1 = Student("Anzar", 20)

s1.show_details()
print("\n")
Student.change_school("XYZ School")
Student.welcome()
print("\n")
s1.show_details()


class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def substract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            return a / b

result1 = Calculator.add(5, 3)
result2 = Calculator.substract(10, 4)
result3 = Calculator.multiply(6, 7)
result4 = Calculator.divide(15, 3)

print("Addition:", result1)
print("Subtraction:", result2)
print("Multiplication:", result3)
print("Division:", result4)



class Even:

    @staticmethod
    def check_even(number):
        if number % 2 == 0:
            return True
        else:
            return False

result1 = Even.check_even(4)
result2 = Even.check_even(7)

print(result1)
print(result2)



class Eligible:

    @staticmethod
    def check_eligibility(age):
        if age >= 18:
            return "Eligible to vote."
        else:
            return "Not eligible to vote."

result1 = Eligible.check_eligibility(20)
result2 = Eligible.check_eligibility(15)
print(result1)
print(result2)


class Bank:

    bank_name = "ABC Bank"

    def __init__(self, name, acc_num, acc_bal):
        self.name = name
        self.acc_num = acc_num
        self.acc_bal = acc_bal

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self.acc_num}")
        print(f"Account Balance: {self.acc_bal}")
        print(f"Bank Name: {self.bank_name}")

    @classmethod
    def change_bank_name(cls, new_bank_name):
        cls.bank_name = new_bank_name

    @staticmethod
    def is_valid_amount(amount):
        if amount > 0:
            print("Valid amount.")
        else:
            print("Invalid amount.")


customer1 = Bank("Anzar", "123456789", 10000)
customer1.show_details()
print("\n")
Bank.change_bank_name("XYZ Bank")
customer1.show_details()
print("\n")
customer1.is_valid_amount(5000)