import random

def main():
    # Generate a random secret number between 1 and 99 (inclusive)
    secret_number = random.randint(1, 99)

    print("I am thinking of a number between 1 and 99...")

    # Initial guess from the user
    guess = int(input("Enter a guess: "))

    # Loop until the guess matches the secret number
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

        print()  # Print an empty line for better readability

        # Prompt the user for a new guess
        guess = int(input("Enter a new guess: "))

    # Congratulate the user when the guess is correct
    print("Congrats! The number was: " + str(secret_number))

# This line is required to call the main() function when the script is executed
if __name__ == '__main__':
    main()
