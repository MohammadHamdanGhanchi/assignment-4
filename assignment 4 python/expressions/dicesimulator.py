"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times. Prints
the results of each die roll. This program is used
to show how variable scope works.
"""

# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print("Total of two dice:", total)

def main():
    die1 = 10  # This is a local variable in main()
    print("die1 in main() starts as:", die1)
    
    # Call roll_dice() three times
    roll_dice()
    roll_dice()
    roll_dice()
    
    # die1 in main remains unchanged
    print("die1 in main() is:", die1)

# Call the main function when the script runs
if __name__ == '__main__':
    main()
