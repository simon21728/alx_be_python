from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in the format: YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()  # Get the current date and time
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """
    Prompt the user to input a number of days and calculate the future date.
    """
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        
        # Calculate the future date
        future_date = datetime.now() + timedelta(days=number_of_days)
        
        # Print the future date in the format: YYYY-MM-DD
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
        
    except ValueError:
        print("Please enter a valid integer for the number of days.")

def main():
    # Display the current date and time
    display_current_datetime()
    
    # Calculate and display the future date based on user input
    calculate_future_date()

if __name__ == "__main__":
    main()

