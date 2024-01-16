#!/usr/bin/python3

# Iterate through the ASCII values of lowercase letters
for i in range(97, 123):
    # Check if the current ASCII value corresponds to 'e' or 'q'
    if i == 101 or i == 113:
        # If 'e' or 'q', skip to the next iteration
        i += 1
        continue
    else:
        # Print the current lowercase letter
        print('{}'.format(chr(i)), end='')
