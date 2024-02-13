#!/usr/bin/python3
"""Rectangle class documentation"""


class Rectangle:
    """Initializes a rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with a specified width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Destructor to print message when a Rectangle instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Returns the width of the instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle instance.

        Args:
            value (int): The width of the rectangle instance.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle instance.

        Args:
            value (int): The height of the rectangle instance.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle instance."""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of a rectangle instance."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns the printable string representation of the rectangle."""
        str_rep = ""
        if self.__width != 0 and self.__height != 0:
            str_rep += "\n".join(str(self.print_symbol) * self.__width
                                 for j in range(self.__height))
        return str_rep

    def __repr__(self):
        """Return a string representation of the rectangle for reproduction."""
        return f"Rectangle({self.__width}, {self.__height})"
