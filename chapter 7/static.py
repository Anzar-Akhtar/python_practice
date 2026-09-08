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