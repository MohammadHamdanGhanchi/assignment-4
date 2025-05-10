def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))

    # Continue doubling the number until it is 100 or greater
    while curr_value < 100:
        print(curr_value, end=" ")  # Print the current value
        curr_value = curr_value * 2   # Double the current value

    # Print the last value that exceeded 100
    print(curr_value)

# This line is required to call the main() function when the script is executed
if __name__ == '__main__':
    main()
