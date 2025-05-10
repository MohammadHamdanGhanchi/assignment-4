MINIMUM_HEIGHT: int = 50  # Arbitrary units for minimum height requirement

def main():
    while True:
        height_input = input("How tall are you? ")  # Prompt for user height
        
        if height_input == "":  # Check for empty input to stop
            print("Exiting the program.")
            break  # Exit the loop if no input
        
        try:
            height = float(height_input)  # Convert input to float
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number for your height.")  # Handle invalid inputs

# This line is required to call the main() function when the script is executed
if __name__ == '__main__':
    main()
