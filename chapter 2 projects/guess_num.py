sec_num = 50

guess = int(input("Guess the number: "))

if guess > sec_num:
    print("Too High")
elif guess < sec_num:
    print("Too Low")
else:
    print("Correct!!")