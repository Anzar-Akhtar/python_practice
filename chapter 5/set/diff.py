A = set(
    int(x) for x in input("Enter 1st group: ").split()
)

B = set(
    int(x) for x in input("Enter 2nd group: ").split()
)

print("Only in 1st:", A - B)
print("Only in 2nd:", B - A)