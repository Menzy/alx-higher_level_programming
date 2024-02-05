#!/usr/bin/python3

def list_division(dividend_list, divisor_list, list_length):
    result = []

    try:
        # Iterate over the lists up to the specified length
        for i in range(list_length):
            try:
                # Get corresponding values from the two lists
                val1 = dividend_list[i]
                val2 = divisor_list[i]

                # Check if the values are of types int or float
                if isinstance(val1, (int, float
                                    )) and isinstance(val2, (int, float)):
                    try:
                        # Perform division and append the result to the result
                        division_result = val1 / val2
                        result.append(division_result)
                    except ZeroDivisionError:
                        # Handle division by zero by appending 0 to the result
                        print("Division by 0")
                        result.append(0)
                else:
                    # Handle wrong type by appending 0 to the result
                    print("Wrong type")
                    result.append(0)
            except IndexError:
                # Handle IndexError by appending 0 to the result
                print("Index out of range")
                result.append(0)
    finally:
        # Return the result
        return result
