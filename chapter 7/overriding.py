# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# animal = Animal()
# dog = Dog()

# animal.sound()
# dog.sound()

# with super

class Animal():
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")

dog = Dog()
dog.sound()


class Vehicle:
    def start(self):
        print("Car is starting")

class Car(Vehicle):
    def start(self):
        print("Car is starting with a key!")

car = Car()
car.start()