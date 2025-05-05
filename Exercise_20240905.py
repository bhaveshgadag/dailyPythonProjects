# (1) The program starts by providing the question and choices and asking the user to pick an answer (1, 2, 3, or 4).
# (2) The user enters a number (e.g., 2). The program prints out “Correct! if the answer is correct.
# (3) The program shows the second question (e.g., Which planet is known as the Red Planet?”). If the user enters 
#     a wrong answer, the program prints the relevant message. The process is repeated with a third question.
# (4) Finally, the program prints out the total score to the user after three questions.

quiz_questions = [
    ("What is the capital of France?", ["Berlin", "Paris", "Madrid", "Rome"], 2),
    ("Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], 3),
    ("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "H2"], 1),
]
score = 0

for question in quiz_questions:
    print(question[0])
    for option in question[1]:
        print(f"{(question[1].index(option))+1}. {option}")
    answer = int(input("Your answer (1/2/3/4): "))
    if answer == question[2]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {question[2]}. {question[1][question[2]-1]}\n")

print(f"Quiz completed! Your final score is {score}/3.")