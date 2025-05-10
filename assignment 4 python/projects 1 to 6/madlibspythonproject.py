def mad_libs():
    print("Welcome to the Mad Libs game!")
    
    # Get inputs from the user
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")
    
    # Create the story using f-strings
    story = f"Once upon a time, a {adjective} {noun} would {verb} {adverb}."
    
    # Print the result
    print("\nHere's your story:")
    print(story)

mad_libs()
