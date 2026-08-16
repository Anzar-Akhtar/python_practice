rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for s in range(1, rows - i - 1):
        print(" ", end="")
    for j in range(1, 2 * i):
        print("*", end="")
    print()