def add_three_copies(my_list, data):
    """Adds three copies of the given data to the provided list."""
    for _ in range(3):
        my_list.append(data)  # Mutably modifies the list by adding the data

########## No need to edit code past this point  ##########

def main():
    message = input("Enter a message to copy: ")  # Get user input
    my_list = []  # Initialize an empty list
    print("List before:", my_list)  # Display the list before modification
    add_three_copies(my_list, message)  # Add three copies of the message to the list
    print("List after:", my_list)  # Display the list after modification

if __name__ == "__main__":
    main()
