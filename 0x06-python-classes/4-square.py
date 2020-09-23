#!/usr/bin/python3
"""Working with Squares"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Creator
        Args:
            size: side of the square
        """
        self.size = size

    @property
    def size(self):
        """Property for the length of a side of this square.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError('size must be an integer')
        if val < 0:
            raise ValueError('size must be >= 0')
        self.__size = val

    def area(self):
        """Area of the new square
        Returns:
            The area
        """
        return self.__size ** 2
