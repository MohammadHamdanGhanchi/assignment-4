MAX_LENGTH: int = 3  # Set the maximum length for the list

def shorten(lst):
    """Removes elements from the end of lst until it contains MAX_LENGTH items."""
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()  # Remove the last element from the list
        print(last_elem)  # Print the removed element

def get_lst():
    """Prompts the user to enter one element of the list at a time and returns the resulting list."""
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    
    while elem != "":
        lst.append(elem)  # Append the entered element to the list
        elem = input("Please enter an element of the list or press enter to stop: ")
    
    return lst

def main():
    lst = get_lst()  # Get the list from user input
    shorten(lst)  # Shorten the list if needed

if __name__ == '__main__':
    main()
