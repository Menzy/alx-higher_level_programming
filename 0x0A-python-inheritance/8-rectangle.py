#!/usr/bin/python3
"""Defines the BaseGeometry and Rectangle classes."""


class BaseGeometry:
    """Creates a class with public instance methods."""

    def area(self):
        """Raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Instantiates a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
