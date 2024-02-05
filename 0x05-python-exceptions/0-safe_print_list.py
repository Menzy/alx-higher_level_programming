#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    # Initialize a counter to keep track of the number of elements printed
    counter = 0

    # Use a try-except block to catch IndexError during the iteration
    try:
        for i in range(x):
            # Print the element without a newline
            print(my_list[i], end="")

            # Increment the counter
            counter += 1
    except IndexError:
        # Catch IndexError if the index is out of bounds
        pass

    # Print a newline after printing the elements
    print()

    # Return the counter value
    return counter
