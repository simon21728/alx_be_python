def daily_reminder():
    # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Handle task priority using match case
    match priority:
        case "high":
            reminder_message = f"'{task}' is a high priority task."
        case "medium":
            reminder_message = f"'{task}' is a medium priority task."
        case "low":
            reminder_message = f"'{task}' is a low priority task."
        case _:
            reminder_message = "Invalid priority level."

    # Modify message based on time-sensitivity
    if time_bound == "yes":
        reminder_message += " It requires immediate attention today!"
    elif time_bound == "no":
        reminder_message += " Consider completing it when you have free time."
    else:
        reminder_message += " Invalid input for time-bound."

    # Print the final reminder message
    print("\nReminder:", reminder_message)


# Call the function to run the reminder
daily_reminder()


