numbers = {i for i in range(1, 6)}
print(numbers)

# Set Comprehension with Condition

even = {i for i in range(1, 11) if i % 2 == 0}
print(even)

# remove duplicates

numbers2 = [1, 2, 2, 3, 3, 4, 5, 5]
unique = {i for i in numbers2}
print(unique)