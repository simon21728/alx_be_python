
def safe_divide(numerator, denominator):
    try:
        # Attempt to convert the inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform the division and return the result with proper message
        result = numerator / denominator
        return f"The result of the division is {result:.1f}"
    
    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."
    
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."

