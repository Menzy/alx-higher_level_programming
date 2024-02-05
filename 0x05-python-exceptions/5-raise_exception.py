#!/usr/bin/python3

def raise_exception():
    try:
        # Raise a TypeError with a custom message
        raise TypeError("Custom type exception")
    except TypeError as e:
        # Catch the raised TypeError and re-raise it
        raise e
