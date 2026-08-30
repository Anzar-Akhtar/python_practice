entry = input("Enter your dairy:-  ")

with open("dairy.txt", "a") as file:
    file.write(entry + "\n")

print("data saved successfully....")
