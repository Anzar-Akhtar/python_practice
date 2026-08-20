nums = []

print("Enter 5 Numbers: ")
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    nums.append(num)

t = tuple(nums)

print("\nYour Tuple:", t)
print("First Element:", t[0])
print("Middle Element:", t[len(t)//2])
print("Last Element:", t[-1])