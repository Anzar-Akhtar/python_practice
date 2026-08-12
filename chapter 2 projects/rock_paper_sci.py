import random

computer = random.randint(1, 3)

user = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))

if user<1 or user>3:
    print("Invalid Choice")

elif user == computer:
    print("Draw")

elif(user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
    print("You Win")

else:
    print("Computer Wins")

print("Computer Choice: ", computer)