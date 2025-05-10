import time

def countdown_timer():
    # Get the countdown time from the user
    total_seconds = int(input("Enter the time in seconds for the countdown: "))
    
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)  # Convert total seconds to minutes and seconds
        timer = f"{mins:02d}:{secs:02d}"  # Format time as MM:SS
        print(timer, end='\r')  # Print the timer on the same line
        time.sleep(1)  # Wait for 1 second
        total_seconds -= 1  # Decrease the total seconds by 1

    print("Time's up!")  # Notify the user when the countdown is complete

countdown_timer()
