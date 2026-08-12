income = float(input("Enter your Income: "))

if income < 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30

rem = income - tax

print("Tax:", tax)
print("Remaining Salary:", rem)