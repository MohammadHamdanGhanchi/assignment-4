import math  # Import the math library to use sqrt()

def main():
    # Get the two perpendicular sides from the user and convert them to floats
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse using the Pythagorean theorem
    bc = math.sqrt(ab**2 + ac**2)

    # Output the length of the hypotenuse
    print(f"The length of BC (the hypotenuse) is: {bc}")

# Required to call the main function when the script is run
if __name__ == '__main__':
    main()
