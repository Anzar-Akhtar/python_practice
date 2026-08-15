num = int(input("Enter a number: "))
original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if rev == original:
    print("Palindrome")
else:
    print("Not a palindrome")