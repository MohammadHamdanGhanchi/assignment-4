# Speed of light in meters per second (constant)
C = 299792458

def main():
    # Ask the user for mass input in kilograms
    mass_in_kg = float(input("Enter kilos of mass: "))

    # Calculate energy using E = m * c^2
    energy_in_joules = mass_in_kg * (C ** 2)

    # Display the results step-by-step
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(energy_in_joules) + " joules of energy!")


# This provided line is required at the end of the file to call main()
if __name__ == '__main__':
    main()
