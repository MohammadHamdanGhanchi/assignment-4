def get_user_numbers():
    """Create an empty list. Ask the user to input numbers and store them in a list.
    Once they enter a blank line, break out of the loop and return the list."""
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        
        # If the user enters a blank line, break out of the loop and stop asking for input
        if user_input == "":
            break
        
        # Convert the user input to an integer and add it to the list
        num = int(user_input)
        user_numbers.append(num)
    
    return user_numbers

def count_nums(num_lst):
    """Create an empty dictionary. Loop over the list of numbers.
    If the number is not in the dictionary, add it as a key with a value of 1.
    If the number is in the dictionary, increment its value by 1."""
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1  # Add the number as a key with an initial count of 1
        else:
            num_dict[num] += 1  # Increment the count for the existing number
    
    return num_dict

def print_counts(num_dict):
    """Loop over the dictionary and print out each key and its value."""
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")  # Formatted print statement

def main():
    """Ask the user to input numbers and store them in a list. Once they enter a blank line,
    print out the number of times each number appeared in the list."""
    user_numbers = get_user_numbers()  # Get user input
    num_dict = count_nums(user_numbers)  # Count occurrences of each number
    print_counts(num_dict)  # Print the results

# Python boilerplate.
if __name__ == '__main__':
    main()
