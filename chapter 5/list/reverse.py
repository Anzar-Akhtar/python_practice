numbers = []

print("Enter 5 numbers: ")
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("\nYour list: ", numbers)
numbers.reverse()
print("Reversed list: ", numbers)