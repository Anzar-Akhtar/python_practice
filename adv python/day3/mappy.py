# map() function kisi iterable (jaise list, tuple) ke har element par ek function apply karta hai.
# Simple meaning: Agar tumhare paas 5 numbers hain aur sabhi ka square calculate karna hai, toh map() use kar sakte ho.

def square(num):
    return num * num

numbers = [1, 2, 3, 4, 5]
result = map(square, numbers)

print(list(result))

# with lambda
result2 = map(lambda x: x*x, numbers)
print(list(result2))

# doubles the numbers
numbers2 = [10, 20, 30, 40, 50]
result3 = map(lambda x: x *2, numbers2)
print(list(result3))

# convert ther string into uppercase()
names = ["aman", "rahul", "riya", "karan"]
res = map(lambda name: name.upper(), names)
print(list(res))

# add the 5 marks in existing marks
marks = [65, 70, 80, 90, 75]
updated_marks = map(lambda x: x+5, marks)
print(list(updated_marks))