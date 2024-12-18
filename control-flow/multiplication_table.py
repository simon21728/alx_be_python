def main():
    # Prompt the user to enter a number for the multiplication table
    number = int(input("Enter a number to see its multiplication table: "))

    # Use a for loop to generate and print the multiplication table from 1 to 10
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

# Run the multiplication table generator
if __name__ == "__main__":
    main()

