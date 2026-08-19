numbers = []

print("Enter 5 Numbers: ")
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)


print("\nYour list: ", numbers)

check = int(input("Enter a number to count its occurences: "))
count = numbers.count(check)


print(f"{check} occurs {count} time(s) in the list.")