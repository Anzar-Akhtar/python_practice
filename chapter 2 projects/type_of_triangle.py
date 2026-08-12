a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or b == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")