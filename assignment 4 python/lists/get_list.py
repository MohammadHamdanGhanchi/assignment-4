def main():
    lst = []  # Make an empty list to store values
    
    val = input("Enter a value: ")  # Get the initial value
    while val:  # Continue while the user input isn't an empty string
        lst.append(val)  # Add the value to the list
        val = input("Enter a value: ")  # Get the next value to add
    
    print("Here's the list:", lst)  # Print the final list after exiting the loop

# This line is required to call the main() function when the script is executed
if __name__ == '__main__':
    main()
