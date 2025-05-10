def main():
    # Dictionary holding the prices of the fruits
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0  # Initialize total cost accumulator

    for fruit_name in fruits:
        price = fruits[fruit_name]  # Get the price of the current fruit
        amount_bought = int(input(f"How many ({fruit_name}) do you want to buy?: "))  # Prompt for quantity
        total_cost += (price * amount_bought)  # Calculate total cost for the current fruit

    # Print the total combined cost, formatted to one decimal place
    print(f"Your total is ${total_cost:.2f}")

# This line is required to call the main() function when the script is executed
if __name__ == '__main__':
    main()
