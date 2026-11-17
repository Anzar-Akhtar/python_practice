# normal
squares = {}
for i in range(1, 6):
    squares[i] = i**2
print(squares)


# comprehension
squares2 = {i: i**2 for i in range(1,6)}
print(squares2)

# Dictionary Comprehension with Condition
even_sqr = {
    i: i**2
    for i in range(1, 11)
    if i % 2 == 0
}
print(even_sqr)