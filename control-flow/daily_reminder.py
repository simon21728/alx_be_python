# Start of the script

# Prompt for a single task
task = input("Enter your task: ")

# Prompt for task priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt for time-bound status
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using match case
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task."
    case "medium":
        reminder_message = f"'{task}' is a medium priority task."
    case "low":
        reminder_message = f"'{task}' is a low priority task."
    case _:
        reminder_message = "Invalid priority level."

# Modify reminder message based on time-sensitivity
if time_bound == "yes":
    reminder_message += " It requires immediate attention today!"
elif time_bound == "no":
    reminder_message += " Consider completing it when you have free time."
else:
    reminder_message += " Invalid input for time-bound."

# Print the final reminder message
print("\nReminder:", reminder_message)

# End of the script


