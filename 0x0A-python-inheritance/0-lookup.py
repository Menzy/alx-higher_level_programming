#!/usr/bin/python3
""" Defines a function 'lookup' to retrieve attributes and methods \
    of an object."""


def lookup(obj):
    """Returns a list of attributes and methods of an object."""
    return dir(obj)
