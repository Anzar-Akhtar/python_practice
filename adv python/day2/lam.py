# normal
def square(num):
    return num * num

print(square(5))

# lambda function
square = lambda num: num * num
print(square(6))

# add
add = lambda a, b: a + b
print(add(10, 20))

# lambda with different arguments
msg = lambda: "Hello Python"
print(msg())

# one argument
double = lambda x: x*2
print(double(4))

# two arguments
mul = lambda a, b: a*b
print(mul(7, 9))

# three arguments
total = lambda a, b, c: a+b+c
print(total(1, 2, 3))

# with else-if
check = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check(6))
print(check(7))

# with sorting
students = [
    ("Aman", 85),
    ("Rahul", 65),
    ("Riya", 95),
    ("Karan", 75)
]
students.sort(key=lambda student: student[1])
print(students)