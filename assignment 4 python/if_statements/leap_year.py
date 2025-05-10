def main():
    # Get the year to check from the user
    year = int(input('Please input a year: '))

    # Check if the year is a leap year
    if year % 4 == 0:  # The year must be divisible by 4
        if year % 100 == 0:  # The year must not be a century or must be divisible by 400
            if year % 400 == 0:  # The year is a leap year if divisible by 400
                print("That's a leap year!")
            else:  # Not divisible by 400
                print("That's not a leap year.")
        else:  # Not divisible by 100
            print("That's a leap year!")
    else:  # Not divisible by 4
        print("That's not a leap year.")

# This line is required to call the main() function when the script is executed
if __name__ == '__main__':
    main()
