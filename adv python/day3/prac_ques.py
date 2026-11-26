from functools import reduce

# q1:- square of number using map()
numbers1 = [1, 2, 3, 4, 5]
res = map(lambda x: x*x, numbers1)
print(list(res))

# q2:- convert all names into uppercase using map()
names = ["aman", "rahul", "riya", "karan"]
res2 = map(lambda name: name.upper(), names)
print(list(res2))

# q3:- filter all even numbers using filter()
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res3 = filter(lambda x: x%2 == 0, numbers2)
print(list(res3))

# q4:- filter all numbers greater than 50
numbers3 = [20, 44, 60, 75, 30, 90, 77]
res4 = filter(lambda x: x>=50, numbers3)
print(list(res4))

# q5:- calculate the sum of all numbers using reduce()
numbers4 = [10, 20, 30, 40, 50]
res5 = reduce(lambda a, b: a+b, numbers4)
print(res5)

# q6:- calculate the product of all numbers using reduce()
res6 = reduce(lambda a,b: a*b, numbers4)
print(res6)




numbers = [10, 20, 30, 40, 50, 60]

# Step 1: Filter numbers greater than 25
filtered = filter(lambda x: x > 25, numbers)

# Step 2: Multiply each number by 2
mapped = map(lambda x: x * 2, filtered)

# Step 3: Calculate total sum
result = reduce(lambda a, b: a + b, mapped)


print("Final Result:", result)