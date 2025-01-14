def safe_divide(numerator, denominator):
    try:
        # Attempt to convert the inputs to floats and perform division
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform the division and return the result
        return numerator/denominator
    
    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."
    
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."

