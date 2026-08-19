numbers = []

print("Enter 5 Numbers: ")
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

total = sum(numbers)
avg = total / len(numbers)

print("\nYour list: ", numbers)
print("Sum of the numbers: ", total)
print("Average of the numbers: ", avg)