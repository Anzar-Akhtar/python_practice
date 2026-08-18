def show_num(*args):
    for num in args:
        print(num)

numbers = [int(x) for x in input("Enter Numbers: ").split()]

show_num(*numbers)