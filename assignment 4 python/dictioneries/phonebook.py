def read_phone_numbers():
    """Ask the user for names/numbers to store in a phonebook (dictionary). Returns the phonebook."""
    phonebook = {}  # Create empty phonebook
    
    while True:
        name = input("Name: ")
        if name == "":  # Check for empty name to stop entering data
            break
        number = input("Number: ")
        phonebook[name] = number  # Store the name-number pair in the phonebook
    
    return phonebook

def print_phonebook(phonebook):
    """Prints out all the names/numbers in the phonebook."""
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")  # Format: Name -> Number

def lookup_numbers(phonebook):
    """Allow the user to lookup phone numbers in the phonebook by looking up the number associated with a name."""
    while True:
        name = input("Enter name to lookup: ")
        if name == "":  # Check for empty input to stop looking up numbers
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook")  # Inform if the name isn't found
        else:
            print(phonebook[name])  # Print the corresponding number

def main():
    phonebook = read_phone_numbers()  # Read names and numbers into the phonebook
    print_phonebook(phonebook)          # Print the entire phonebook
    lookup_numbers(phonebook)           # Enable lookup for numbers by name

# Python boilerplate. This ensures the main function runs when the script is executed.
if __name__ == '__main__':
    main()
