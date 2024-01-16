#!/usr/bin/python3

# Loop through ASCII values for lowercase letters
for character in range(97, 123):
    # Check if the current character is 'e' or 'q'
    if character == 101 or character == 113:
        # Skip printing 'e' and 'q'
        continue
    # Print the current character
    print("{:c}".format(character), end='')
