def total(*args):

    result = 0

    for i in args:
        result += i

    return result

numbers = [int(x) for x in input("Enter Numbers: ").split()]

answer = total(*numbers)
print("Total:", answer)