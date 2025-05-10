MAX_TERM_VALUE: int = 10000

def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number

    # Continue generating and printing Fibonacci terms while the current term is less than or equal to the max value
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Print the current term followed by a space

        # Calculate the next term in the sequence
        term_after_next = curr_term + next_term

        # Update terms for the next iteration
        curr_term = next_term
        next_term = term_after_next

# This line is required to call the main() function when the script is executed
if __name__ == '__main__':
    main()
