def get_last_element(lst):
    """Prints the last element of the provided list."""
    # Print the last element using negative indexing
    print(lst[-1])  # This is the most concise way to get the last element

def get_lst():
    """Prompts the user to enter one element of the list at a time and returns the resulting list."""
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    
    return lst

def main():
    lst = get_lst()  # Get the list from user input
    get_last_element(lst)  # Print the last element of the list

if __name__ == '__main__':
    main()
