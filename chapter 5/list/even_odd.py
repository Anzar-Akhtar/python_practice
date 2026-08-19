numbers = []

print("Enter 5 numbers: ")
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("\nYour list: ", numbers)

even = []
odd = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("\nYour list: ", numbers)
print("Even numbers: ", even)
print("Odd numbers: ", odd)