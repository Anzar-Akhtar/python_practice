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