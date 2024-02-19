#!/usr/bin/python3
"""Defines the BaseGeometry class."""


class BaseGeometry:
    """Creates the BaseGeometry class."""

    def area(self):
        """Calculate the area. Raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The integer value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
