def fact(num):
    result = 1

    for i in range(1, num + 1):
        result *= i

    return result

n = int(input("Enter a number to calculate its factorial: "))
print("The factorial of", n, "is:", fact(n))