numbers = []

print("Enter 10 Integers: ")
for i in range(10):
    n = int (input(f"Number {i+1}: "))
    numbers.append(n)

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("\nOriginal list:", numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)
print("Total even:", len(even))
print("Total odd:", len(odd))