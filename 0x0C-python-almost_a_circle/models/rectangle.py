#!/usr/bin/python3
"""
module defines a rectangle class
and inherits from base
"""
from models.base import Base


class Rectangle(Base):
    """this defines a rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor for the rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieves the value for width"""
        return self.__width

    @property
    def height(self):
        """retrieves the value for height"""
        return self.__height

    @property
    def x(self):
        """retrieves the value for x"""
        return self.__x

    @property
    def y(self):
        """retrieves the value for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """sets the value for width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """sets the value for height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """sets the value for x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """sets the value for y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """defines the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """represents the rectangle with #"""
        if self.width == 0 or self.height == 0:
            return ""

        for x in range(self.y):
            print()

        for y in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        defines a a string format
        representation of the class
        """
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """update assigns an argument to attribute"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """returns the dictionary representation of a rectangle"""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
