#!/usr/bin/python3

def raise_exception_msg(message=""):
    try:
        # Raise a NameError with the specified message
        raise NameError(message)
    except NameError as e:
        # Catch the raised NameError and re-raise it
        raise e
