# reduce() function iterable ke multiple elements ko combine karke ek single value produce karta hai.

# Iske liye humein functools module se reduce() import karna hota hai.

from functools import reduce


# calculate the sum of the list
numbers = [10, 20, 30, 40, 50]
result = reduce(lambda a, b: a+b, numbers)
print(result)

# multiplication of all numbers
result2 = reduce(lambda a, b: a*b, numbers)
print(result2)

# find maximum number
result3 = reduce(lambda a, b: a if a>b else b, numbers)
print(result3)