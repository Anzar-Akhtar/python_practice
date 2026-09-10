# class Animal:

#     def eat(self):
#         print("Animal is eating.")

# class Dog(Animal):
#     pass

# dog1 = Dog()
# dog1.eat()


# class Vehicle:

#     def start(self):
#         print("Vehicle is starting.")


# class Car(Vehicle):

#     def drive(self):
#         print("Car is driving.")

# car1 = Car()

# car1.start()
# car1.drive()


# class Person:

#     def __init__(self, name):
#         self.name = name

#     def show_name(self):
#         print(f"Name: {self.name}")

# class Student(Person):

#     def study(self):
#         print(f"{self.name} is studying.")

# stu1 = Student("Alice")

# stu1.show_name()
# stu1.study()


class Animal:

    def eat(self):
        print("Animal is eating.")

class Dog(Animal):

    def bark(self):
        print("Dog is barking")

animal = Dog()

animal.eat()
animal.bark()