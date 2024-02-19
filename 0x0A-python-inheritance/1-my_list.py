#!/usr/bin/python3
"""Defines the MyList class, a subclass of the built-in list class."""


class MyList(list):
    """A custom list class that inherits from the built-in list class."""

    def print_sorted(self):
        """Prints the elements of the list instance in sorted order."""
        print(sorted(self))
