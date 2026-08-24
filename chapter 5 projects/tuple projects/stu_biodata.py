print("Enter Student details: ")
name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")
course = input("Course: ")

student = (name, age, city, course)

print("\n--- Student Bio Data ---")
print("Name:", student[0])
print("Age:", student[1])
print("City:", student[2])
print("Course:", student[3])