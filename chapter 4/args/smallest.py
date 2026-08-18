def smallest(*args):

    smallest = args[0]

    for i in args:
        if i < smallest:
            smallest = i

    return smallest

numbers = [int(x) for x in input("Enter Numbers: ").split()]

result = smallest(*numbers)

print("Smallest:", result)