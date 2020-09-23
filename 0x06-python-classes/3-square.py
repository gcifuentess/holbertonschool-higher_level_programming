#!/usr/bin/python3
"""Working with Squares"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Creator
        Args:
            size: side of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area of the new square
        Returns:
            The area
        """
        return self.__size ** 2
