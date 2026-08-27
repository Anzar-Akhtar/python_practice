A = set(
    int(x) for x in input("Enter first group: ").split()
)

B = set(
    int(x) for x in input("Enter second group: ").split()
)

common = A & B

print("Common numbers: ", common)