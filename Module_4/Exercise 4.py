import random

guess = float(input("Guess a number between 1 and 10: "))
number = random.randint(1, 10)

while guess != number:

    if guess > number:
        print("Too high!")

    elif guess < number:
        print("Too low!")
    guess = float(input("Guess another number between 1 and 10: "))

print("Yahoo! Correct answer.")

