def main():
    # Prompt the user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Start building the reminder message
    reminder = f"Reminder: '{task}'"

    # Use match case to determine the priority level
    match priority:
        case "high":
            reminder += " is a high priority task"
        case "medium":
            reminder += " is a medium priority task"
        case "low":
            reminder += " is a low priority task"
        case _:
            reminder += " has an invalid priority level. Please choose 'high', 'medium', or 'low'."

    # Modify reminder based on whether the task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += " (Invalid input for time-bound status)."

    # Output the final reminder
    print(reminder)

# Run the daily reminder script
if __name__ == "__main__":
    main()

