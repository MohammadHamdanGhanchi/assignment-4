def main():
    ali = 21  # Ali's age is given as 21 years old
    ahmed = ali + 6  # Ahmed is 6 years older than Anton
    abdullah = ahmed + 20  # Abdullah is 20 years older than Beth
    shahid = abdullah + ali  # Shahid is as old as Chen's age plus Anton's age
    hamdan = abdullah  # Hamdan is the same age as Chen

    # Print out all of the ages exactly as required
    print("Ali is " + str(ali))
    print("Ahmed is " + str(ahmed))
    print("Abdullah is " + str(abdullah))
    print("Shahid is " + str(shahid))
    print("Hamdan is " + str(hamdan))


# This line ensures the main function runs when the script is executed
if __name__ == '__main__':
    main()
