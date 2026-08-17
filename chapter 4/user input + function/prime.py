def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False 

    return True


n = int(input("Enter a number to check if it's prime: "))

if is_prime(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")