from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map(): square of each numbers
result1 = map(lambda x: x*x, numbers)
print(list(result1))

# filter():- Only even numbers
result2 = filter(lambda x: x%2 == 0, numbers)
print(list(result2))

# reduce():- sum of all numbers
result3 = reduce(lambda a, b: a+b, numbers)
print(result3)