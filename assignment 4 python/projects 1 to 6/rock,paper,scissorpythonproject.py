import random

def rock_paper_scissors():
    # Define the possible options
    choices = ["rock", "paper", "scissors"]
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose your option: Rock, Paper or Scissors")

    # Get user input
    user_choice = input("Enter your choice: ").lower()

    # Validate user input
    if user_choice not in choices:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        return

    # Computer randomly chooses
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

rock_paper_scissors()
