#!/usr/bin/python3

def remove_char_at(str, n):
    # Check if the index is negative
    if n < 0:
        # If negative, return the original string unchanged
        return str

    # Return a new string with the character at index n removed
    return (str[0:n] + str[n + 1:])
