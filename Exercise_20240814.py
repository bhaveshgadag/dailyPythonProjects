# When the user executes the program, the program prompts the user to 
# guess a number between 1 and 100 in the terminal.
# The user types in a number and the program gives feedback on whether 
# that number is too low or too high from the hidden number so the user 
# can adjust the next number.
# The user can submit up to 10 numbers until they win or fail. 

import random

print("Welcome to the Number Guessing Game!")

number = random.randint(1,100)

print("""I have selected a number between 1 and 100
You have 10 attempts to guess the number""")

attempt = 0

while attempt < 10:
    guess = int(input("Enter your guess: "))
    attempt += 1

    if guess == number:
        print(f"Congralutions! You have guessed the correct number in {attempt} attempts.")
        break
    elif guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")

if attempt == 10:
    print("You failed to guess the correct number. Better luck next time.")
    print(f"The number was {number}.")