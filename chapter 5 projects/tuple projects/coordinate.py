import math

print("Enter first point(x1, y1):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
point1 = (x1, y1)

print("Enter second point(x2, y2):")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
point2 = (x2, y2)


distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

print("\nPoint 1:", point1)
print("Point 2:", point2)
print("Distance between points:", distance)