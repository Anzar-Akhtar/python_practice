numbers = []

print("Enter 4 Numbers: ")
for i in range(4):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("\nOriginal list:", numbers)

end = int(input("Enter a numbr to add at the end: "))
numbers.append(end)

pos = int(input("Enter a number to insert at pos 2: "))
numbers.insert(1, pos)

print("Updated list:", numbers)