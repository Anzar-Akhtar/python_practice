A = set(
    int(x) for x in input("Enter 1 group: ").split()
)

B = set(
    int(x) for x in input("Enter 2 group: ").split()
)

result = A | B

print("All unique numbers: ", result)