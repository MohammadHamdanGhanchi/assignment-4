import random  # Import the random library

N_NUMBERS: int = 10  # Number of random numbers to generate
MIN_VALUE: int = 1   # Minimum random value
MAX_VALUE: int = 100 # Maximum random value

def main():
    # Generate and print 10 random numbers in the specified range
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]  # List comprehension to generate random numbers
    print(" ".join(map(str, random_numbers)))  # Print numbers space-separated

# This line is required to call the main() function when the script is executed
if __name__ == '__main__':
    main()
