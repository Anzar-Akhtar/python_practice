def count_even(*args):

    count = 0
    

    for i in args:
        if i % 2 == 0:
            count += 1
    return count


numbers = [int(x) for x in input("Enter Numbers: ").split()]

result = count_even(*numbers)
print(f"The count of even numbers is: {result}")