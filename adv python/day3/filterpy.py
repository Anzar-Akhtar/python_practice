# filter() function kisi iterable mein se sirf un elements ko select karta hai jo given condition satisfy karte hain.

# Simple meaning: Agar list mein 10 numbers hain aur tumhe sirf even numbers chahiye, toh filter() use kar sakte ho.

# find even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))

# numbers greater than 50
marks = [25, 45, 60, 75, 30, 90, 85]
result2 = filter(lambda x: x > 50, marks)
print(list(result2))

# names start with A
names = ["Aman", "Rahul", "Ankit", "Riya", "Arjun"]
result3 = filter(lambda name: name.startswith("A"), names)
print(list(result3))

# Positive numbers
numbers2 = [-10, 20, -5, 30, 0, 15, -2]
result4 = filter(lambda x: x > 0, numbers2)
print(list(result4))

# Student who passed
marks = [85, 32, 45, 90, 28, 76]
result5 = filter(lambda x: x >= 40, marks)
print(list(result5))