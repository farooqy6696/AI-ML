#5. Create a Number Guessing Game where:

# The program generates a random number between 1 and 50 using random.
# The user has 5 attempts to guess the number.
# After each guess, calculate the absolute difference using math.fabs() and display how far the guess is from the correct number.

import random
import math

secret_number = random.randint(1, 50)

attempts = 5

for i in range(attempts):
    guess = int(input("Enter your guess (1-50): "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        difference = math.fabs(secret_number - guess)
        print("Wrong guess!")
        print("You are", difference, "away from the correct number.")

else:
    print("Game Over!")
    print("The correct number was:", secret_number)