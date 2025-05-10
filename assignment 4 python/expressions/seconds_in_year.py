# Useful constants to help make the math easier and cleaner!
DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MIN_PER_HOUR = 60
SEC_PER_MIN = 60

def main():
    # Calculate the number of seconds in a year
    total_seconds_in_year = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    
    # Print the result in a nice format
    print(f"There are {total_seconds_in_year} seconds in a year!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
