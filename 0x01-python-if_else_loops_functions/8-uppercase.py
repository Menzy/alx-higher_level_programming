#!/usr/bin/python3

def uppercase(str):
    # Iterate through the characters of the input string
    for i in range(len(str)):
        # Get the ASCII value of the current character
        a = ord(str[i])

        # Check if the ASCII value corresponds to a lowercase letter
        if a >= 97 and a <= 123:
            # Convert the lowercase letter to uppercase by subtracting 32
            a = a - 32

        # Print the character (either as is or converted to uppercase)
        print("{}".format(chr(a)), end='')

    # Print a newline after processing all characters in the string
    print()
