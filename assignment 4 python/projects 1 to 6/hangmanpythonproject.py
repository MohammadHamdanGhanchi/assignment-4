import random

def hangman():
    # Initialize the list of words and choose a random one
    words = ["python", "hangman", "challenge", "programming", "computer"]
    word_to_guess = random.choice(words)
    word_length = len(word_to_guess)
    
    # Create a list to track the correct guesses and a set for guessing letters
    guessed_letters = []
    attempts = 6  # Number of allowed incorrect attempts
    display_word = ["_"] * word_length  # Display word initialized with underscores

    print("Welcome to Hangman!")
    print("Guess the word:")
    print(" ".join(display_word))

    # Game loop
    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():  # Validate input
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:  # Check if letter has already been guessed
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:  # Correct guess
            for index, letter in enumerate(word_to_guess):
                if letter == guess:
                    display_word[index] = guess
            
            print(f"Good guess! Current word: {' '.join(display_word)}")
        else:  # Incorrect guess
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        if "_" not in display_word:  # Check if the word has been completely guessed
            print(f"Congratulations! You've guessed the word: {word_to_guess}")
            break
    else:  # If the loop ends without breaking, the player has run out of attempts
        print(f"Game over! The word was: {word_to_guess}")

hangman()
