#!/usr/bin/python3
"""Working with rectangles."""


class Rectangle:
    """Defines a Rectangle."""

    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1

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
        """Area of the this rectangle.
        Returns:
            The area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of this rectangle.
        Returns:
            The perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self):
        """Creates the string of the new rectangle represented with symbol.
        Returns:
            The string of symbols with the shape of this rectangle.
        """
        str_rect = ""
        if not self.__width or not self.__height:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                str_rect += str(self.print_symbol)
            if (i + 1) < self.__height:
                str_rect += "\n"
        return str_rect

    def __repr__(self):
        """Creates the string that can recreate the actual rectangle.
        Returns:
            The string that can recreate the actual rectangle.
        """
        repr_rect = ("Rectangle(" + str(self.__width) + ", " +
                     str(self.__height) + ")")
        return repr_rect

    def __del__(self):
        """Hendles when an instance is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """finds the biggest rectangle based on the area.
        Args:
            rect_1: The first rectangle.
            rect_2: The second rectangle.
        Raises:
            TypeError: If rect_1, rect_2 are not instances of Rectangle.
        Returns:
            The biggest rectangle.
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """new Rectangle instance with width == height == size.
        Args:
            size: size of the desired square.
        Returns:
            New rectangle.
        """
        return cls(size, size)
