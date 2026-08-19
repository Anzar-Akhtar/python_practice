numbers = []

print("Enter 5 Numbers: ")
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("\nYour list: ", numbers)

val = int(input("\nEnter a number to remove from the list: "))
if val in numbers:
    numbers.remove(val)
    print(f"{val} has been removed from the list.")
else:
    print(f"{val} is not in the list.")

print("Updated list: ", numbers)