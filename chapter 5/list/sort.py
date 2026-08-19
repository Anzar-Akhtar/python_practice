numbers = []

print("Enter 5 Numbers: ")
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)


print("\nYour list: ", numbers)
asc = sorted(numbers)
dsc = sorted(numbers, reverse=True)

print("Ascending order: ", asc)
print("Descending order: ", dsc)