def main():
    print("This program adds two numbers.")
    
    # Prompt user for first number and convert to int
    num1 = int(input("Enter first number: "))
    
    # Prompt user for second number and convert to int
    num2 = int(input("Enter second number: "))
    
    # Calculate the sum
    total = num1 + num2
    
    # Print the result
    print("The total is " + str(total) + ".")

# This line ensures main() runs when the script is executed
if __name__ == '__main__':
    main()
