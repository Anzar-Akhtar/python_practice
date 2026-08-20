nums = []
print("Enter 5 numbers: ")
for i in range(5):
    num = int(input(f"enter number {i + 1}: "))
    nums.append(num)


t = tuple(nums)

total = sum(t)
avg = total / len(t)

print("\nYour tuple:", t)
print("Sum:", total)
print("Average:", avg)