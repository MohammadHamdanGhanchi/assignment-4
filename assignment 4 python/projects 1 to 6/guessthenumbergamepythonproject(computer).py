import random

def guess_the_number():
    number = random.randint(1, 100)  # Computer selects a random number between 1 and 100
    guess = None  # Initialize the guess variable

    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != number:  # Continue looping until the guess is correct
        guess = int(input("Make a guess: "))  # Get user input

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number.")

guess_the_number()
