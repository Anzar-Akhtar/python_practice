numbers = []

print("Enter 10 integers: ")
for i in range(10):
    n = int(input(f"Number {i+1}: "))
    numbers.append(n)

positive = []
negative = []
zero = []

for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero.append(num)

print("\nOriginal list:", numbers)
print("Positive numbers:", positive, "| Count:", len(positive))
print("Negative numbers:", negative, "| Count:", len(negative))
print("Zeros:", zero, "| Count:", len(zero))