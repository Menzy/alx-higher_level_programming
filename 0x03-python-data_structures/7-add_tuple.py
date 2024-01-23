#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples element-wise and returns a new tuple.

    Parameters:
        tuple_a (tuple): The first input tuple.
        tuple_b (tuple): The second input tuple.

    Returns:
        tuple: A new tuple containing the sum of the input tuples.
    """
    # Convert tuples to lists for easier manipulation
    list_a, list_b = list(tuple_a), list(tuple_b)

    # Ensure each tuple has at least two elements
    if len(tuple_a) < 2:
        list_a.extend([0] * (2 - len(tuple_a)))
    if len(tuple_b) < 2:
        list_b.extend([0] * (2 - len(tuple_b)))

    # Truncate lists to the first two elements
    list_a = list_a[:2]
    list_b = list_b[:2]

    # Element-wise addition
    new_list = [list_a[0] + list_b[0], list_a[1] + list_b[1]]

    # Convert the result back to a tuple
    new_tuple = tuple(new_list)

    return new_tuple
