questions = [
    ["what is the Capital of India?", "delhi"],
    ["2 + 2", "4"],
    ["Python creator?", "guido"],
    ["what is the Capital of USA?", "washington"],
    ["what is the Capital of UK?", "london"],
]

name = input("Enter your name: ")

score = 0

for question in questions:

    answer = input(question[0] + " ")

    if answer.lower() == question[1].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\n ===== RESULT =====")

print("Name: " + name)
print("Score: ", score, "/", len(questions))


with open("quiz_results.txt", "a") as file:
    file.write(name + " - " + str(score) + "/" + str(len(questions)) + "\n")

print("Result saved successfully!")