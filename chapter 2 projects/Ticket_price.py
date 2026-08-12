age = int(input("Enter your age: "))

if age < 5:
    price = 0
    print("Ticket is free for you")
elif age <= 18:
    price = 100
elif age <= 60:
    price = 200
else:
    price = 150

print("Ticket Price:", price)