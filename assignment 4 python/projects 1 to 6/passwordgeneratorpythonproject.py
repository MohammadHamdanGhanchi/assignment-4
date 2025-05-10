import random
import string

def generate_password(length):
    # Define the characters to include in the passwords
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))  # Generate password
    return password

def password_generator():
    # Get user input for number of passwords and their length
    num_passwords = int(input("How many passwords would you like to generate? "))
    password_length = int(input("Enter the length of each password: "))

    # Generate and display the passwords
    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        print(generate_password(password_length))

password_generator()
