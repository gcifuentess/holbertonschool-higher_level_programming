#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size):
        """Constructor.
        Args:
            size: length of a side of the square.

        Raises:
            ValueError: If size is less than 0
            TypeError: If size is not integer
        """
        if size < 0:
            raise ValueError('size must be >= 0')
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        self.__size = size
