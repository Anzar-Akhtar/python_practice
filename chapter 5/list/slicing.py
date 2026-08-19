numbers = []

print("Enter 6 Numbers: ")
for i in range(6):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

mid = len(numbers) // 2

first_half = numbers[:mid]
second_half = numbers[mid:]


print("\nYour list: ", numbers)
print("First half of the list: ", first_half)
print("Second half of the list: ", second_half)