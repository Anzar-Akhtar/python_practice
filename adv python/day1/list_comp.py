# normal

numbers = []
for i in range(1, 11):
    numbers.append(i)

print(numbers)

# comprehension

new_list = [i for i in range(1, 11)]
print(new_list)


# LIST COMPREHENSION WITH CONDITION

# normal

even = []
for i in range(1, 11):
    if i % 2 == 0:
        even.append(i)

print(even)

# comprehension
new_even = [i for i in range(1, 11) if i % 2 == 0]
print(new_even)


# LIST COMPREHENSION WITH EXPRESSION

# normal

squares = []
for i in range(1, 11):
    squares.append(i ** 2)

print(squares)


# comprehension 
new_sq = [i**2 for i in range(1, 11)]
print(new_sq)

# LIST COMPREHENSION WITH IF-ELSE
result = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 6)]
print(result)