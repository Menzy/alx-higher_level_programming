#!/usr/bin/python3

def safe_print_division(a, b):
    result = None

    try:
        # Attempt to perform the division
        result = a / b
    except ZeroDivisionError:
        # Catch ZeroDivisionError if division by zero occurs
        return None
    finally:
        # Print the value of the result (even if it's None)
        print("Inside result: {}".format(result))

        # Return the result (it could be None if there was a ZeroDivisionError)
        return result
