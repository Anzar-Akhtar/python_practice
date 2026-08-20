nums= []

print("Enter 5 numbers: ")
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    nums.append(num)

t = tuple(nums)

print("\nThe tuple is:", t)