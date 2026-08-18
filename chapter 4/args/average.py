def avg(*args):

    total = 0

    for i in args:
        total += i

    return total / len(args)


numbers = [int(x) for x in input("Enter Numbers: ").split()]

result = avg(*numbers)

print(f"The average of the numbers is: {result}")