#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    # Initialize a counter to keep track of the number of integers printed
    counter = 0

    try:
        # Iterate over the elements up to index x
        for i in range(x):
            # Check if the element is an integer
            if isinstance(my_list[i], int):
                # If it's an integer, print it without a newline
                print("{:d}".format(my_list[i]), end="")

                # Increment the counter
                counter += 1
    except (ValueError, TypeError):
        # Catch ValueError or TypeError if they occur during the iteration
        pass

    # Print a newline after printing the integers
    print()

    # Return the counter value
    return counter
