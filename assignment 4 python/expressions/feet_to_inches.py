"""
An example program with constants
"""

# Constant: number of inches in one foot
INCHES_IN_FOOT = 12

def main():
    # Ask user to input feet
    feet = float(input("Enter number of feet: "))
    
    # Convert feet to inches
    inches = feet * INCHES_IN_FOOT
    
    # Display the result
    print("That is", inches, "inches!")

# Required to call main function when program runs
if __name__ == '__main__':
    main()
