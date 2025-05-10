import random

def computer_guess():
    low = 1
    high = 100
    feedback = ""
    
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    
    while feedback != "c":  # Continue guessing until the user indicates the correct guess
        guess = random.randint(low, high)  # Computer makes a guess
        print(f"My guess is: {guess}")
        
        feedback = input("Enter 'h' if my guess is too high, 'l' if it's too low, or 'c' if I got it correct: ").lower()
        
        if feedback == "h":
            high = guess - 1  # Adjust the upper bound
        elif feedback == "l":
            low = guess + 1  # Adjust the lower bound
        elif feedback == "c":
            print("Yay! I guessed your number!")
        else:
            print("Please enter 'h', 'l', or 'c'.")

computer_guess()
