def main():
    # Ask the user for the size of the pattern (positive integer)
    size = int(input("Enter the size of the pattern: "))

    # Ensure the input is a positive integer
    if size <= 0:
        print("Please enter a positive integer.")
        return

    # Use a while loop to iterate through each row
    row = 0
    while row < size:
        # Use a for loop to print the stars in each row
        for col in range(size):
            print("*", end="")
        # After printing all stars in the row, print a newline to move to the next row
        print()
        row += 1

# Run the pattern drawing function
if __name__ == "__main__":
    main()

