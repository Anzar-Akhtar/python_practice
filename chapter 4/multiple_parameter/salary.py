def salary(basic, bonus, deduction):
    final_salary = basic + bonus - deduction
    print("Final Salary: ", final_salary)

basic = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus amount: "))
deduction = float(input("Enter deduction amount: "))
salary(basic, bonus, deduction)