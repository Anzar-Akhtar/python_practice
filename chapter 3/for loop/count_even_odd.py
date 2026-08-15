n = int(input("Enter N: "))

even_count = 0
odd_count = 0

for i in range(1, n+1):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even count:", even_count)
print("Odd count:", odd_count)