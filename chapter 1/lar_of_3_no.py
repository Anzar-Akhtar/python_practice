a = int(input("Enter the first no.: "))
b = int(input("Enter the second no.: "))
c = int(input("Enter the third no.: "))

if(a>b and b>c):
    print("Largest no. is: ", a)

elif(b>a and b>c):
    print("Largest no. is: ", b)

else:
    print("Largest no. is: ", c)
    