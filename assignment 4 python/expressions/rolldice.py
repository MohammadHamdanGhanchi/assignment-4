"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""
# Import the random library to simulate random things like dice rolls
import random

# Number of sides on each die to roll
NUM_SIDES = 6

def main():
    # Roll two dice, each with NUM_SIDES sides
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    
    # Calculate the total of the two dice
    total = die1 + die2
    
    # Print the results
    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

# This line is required at the end to call main()
if __name__ == '__main__':
    main()
