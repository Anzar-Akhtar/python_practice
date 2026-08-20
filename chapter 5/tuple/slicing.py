nums = []

print("Enter 6 numbers: ")
for i in range(6):
    num = int(input(f"Enter number {i + 1}: "))
    nums.append(num)


t = tuple(nums)
print("\nYour tuple:", t)
print("Sliced tuple (first 3 elements):", t[0:3])
print("Sliced tuple (last 3 elements):", t[3:6])