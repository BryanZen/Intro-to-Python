# A simple number-guessing game

import random

target = random.randint(1,10) # The number to guess

chances = 3

# "prime" the loop by collecting a starting guess from the user
guess = int(input("What's your guess? "))

# Repeat until the user correctly guesses the number
while guess != target and chances > 1:
    chances = chances - 1 # We used up a guess
    print("BZZT! Wrong! Try again...")
    if guess > target:
        print("Your guess was too high.")
    else:
        print("Your guess was too low.")
    print("You have", chances, "guesses left.")
    guess = int(input("GUess again: "))
    # Target = random.randit(1,10) # Cruelly reset the secret number

if guess == target:
    print("Congratulations! You successfully guessed the secret number!")
else:
    print("Sorry! The secret number was", target)
