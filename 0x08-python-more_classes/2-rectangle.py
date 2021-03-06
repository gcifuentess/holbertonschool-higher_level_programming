#!/usr/bin/python3
"""Working with rectangles."""


class Rectangle:
    """Defines a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle.
        Args:
            width: the longest side of the rectangle.
            height: the shortest side of the rectangle.
        Return:
            An instance of a Rectangle with width and height.
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """Property for the height of this rectangle.
        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is int:
            if val >= 0:
                self.__height = val
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """Property for the width of this rectangle.
        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) is int:
            if val >= 0:
                self.__width = val
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    def area(self):
        """Area of the new rectangle.
        Returns:
            The area
        """
        return self.__width * self.height

    def perimeter(self):
        """Perimeter of the new rectangle.
        Returns:
            The perimeter
        """
        if self.__width == 0 or self.height == 0:
            return 0
        else:
            return self.__width * 2 + self.height * 2
