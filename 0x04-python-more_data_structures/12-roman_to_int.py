#!/usr/bin/python3

def roman_to_int(roman_string):
    # Check if the input is None or not a string
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    # Dictionary mapping Roman numerals to integers
    key = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    res = 0
    r_length = len(roman_string)

    for i in range(r_length - 1):
        # If the current numeral is smaller than the next, subtract its value
        if key[roman_string[i]] < key[roman_string[i + 1]]:
            res -= key[roman_string[i]]
        else:
            res += key[roman_string[i]]

    # Add the value of the last numeral
    res += key[roman_string[-1]]

    return res
