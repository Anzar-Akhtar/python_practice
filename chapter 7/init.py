class Employee:

    def __init__(self, name, age, salary, department):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department

em1 = Employee("Anzar", 20, 30000, "IT")
em2 = Employee("Atah", 18, 25000, "Finance")
em3 = Employee("Aaira", 17, 30000, "Management")

print("\n==== Employee 1 Details ===")
print(em1.name)
print(em1.age)
print(em1.salary)
print(em1.department)

print("\n==== Employee 2 Details ===")
print(em2.name)
print(em2.age)
print(em2.salary)
print(em2.department)

print("\n==== Employee 3 Details ===")
print(em3.name)
print(em3.age)
print(em3.salary)
print(em3.department)


class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

stu1 = Student("Anzar", 20, "BCA")

print(stu1.name)
print(stu1.age)
print(stu1.course)



class Car:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}")

    def start(self):
        print(f"{self.brand} {self.model} is starting....")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping....")

car1 = Car("Toyota", "Fortuner", 4000000)
car2 = Car("Honda", "Civic", 2500000)

car1.show_details()
car1.start()
car1.stop()

print("\n")

car2.show_details()
car2.start()
car2.stop()




class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

    def study(self):
        print(f"{self.name} is studying .....")

    def sleep(self):
        print(f"{self.name} is sleeping .....")


student1 = Student("Tony", 28, "B.Tech")
student2 = Student("Mony", 26, "M.Tech")

student1.show_details()
student1.study()
student1.sleep()

print("\n")

student2.show_details()
student2.study()
student2.sleep()



class Employee:

    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {self.company}")

em1 = Employee("Anzar", 30000)
em2 = Employee("Atah", 35000)

em1.show_details()
print("\n")
em2.show_details()