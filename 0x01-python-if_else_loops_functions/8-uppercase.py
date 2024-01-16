#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        # Check if the character is a lowercase letter
        if 97 <= ord(char) <= 122:
            # Convert the lowercase letter to uppercase and print it
            print("{}".format(chr(ord(char) - 32)), end='')
        else:
            # Print the character as is if it's not a lowercase letter
            print("{}".format(char), end='')

    # Print a new line after processing the entire string
    print()
