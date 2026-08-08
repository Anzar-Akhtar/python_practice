units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = units * 7 
else:
    bill = units * 10

print("Electricity Bill: ", bill)