# polymorphism:- Yaani ek hi naam ka method different objects ke liye different kaam kar sakta hai.

class Dog:

    def sound(self):
        print("Dog barks")

class Cat:

    def sound(self):
        print("Cat meow")

class Cow:

    def sound(self):
        print("Cow moo")

dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
cat.sound()
cow.sound()


class Car:

    def move(self):
        print("Car is driving")

class Plane:
    def move(self):
        print("Plane is flying")


car = Car()
plane = Plane()

def star_moving(vehicle):
    vehicle.move()

star_moving(car)
star_moving(plane)


class Student:

    def work(self):
        print("Student is studing")

class Teacher:

    def work(self):
        print("Teacher is teaching")


stu = Student()
teacher = Teacher()

def perform_work(person):
    person.work()

perform_work(stu)
perform_work(teacher)