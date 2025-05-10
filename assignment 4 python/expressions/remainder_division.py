def main():
    # Get the numbers we want to divide
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))

    # Calculate the quotient (integer division)
    quotient = dividend // divisor  # Integer division (quotient)
    
    # Calculate the remainder (modulo operation)
    remainder = dividend % divisor  # Remainder of the division
    
    # Display the result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# This line is required to call the main() function when running the script
if __name__ == '__main__':
    main()
