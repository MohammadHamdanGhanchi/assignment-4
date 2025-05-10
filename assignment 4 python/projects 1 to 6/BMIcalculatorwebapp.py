def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Convert height to meters
    bmi = weight / (height_m ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("=== BMI Calculator ===")
    try:
        height = float(input("Enter your height in cm: "))
        weight = float(input("Enter your weight in kg: "))
        
        if height <= 0 or weight <= 0:
            print("Height and weight must be positive numbers.")
            return

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
