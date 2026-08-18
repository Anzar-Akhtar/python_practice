def largest(*args):

    largest = args[0]

    for i in args:
        if i > largest:
            largest = i

    return largest

numbers = [int(x) for x in input("Enter Numbers: ").split()]

result = largest(*numbers)

print("Largest:", result)