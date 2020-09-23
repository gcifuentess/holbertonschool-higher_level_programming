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

    @property
    def position(self):
        """Property for the position of this square.
        Raises:
            TypeError: If value is not tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, val):
        if not isinstance(val, tuple) or len(val) != 2 or \
         len([x for x in val if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = val

    def my_sprint(self):
        """string formating of the square"""
        ret = ""
        if not self.size:
            return "\n"

        for i in range(self.position[1]):
                ret += "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                ret += " "
            for j in range(self.size):
                ret += "#"
            ret += "\n"
        return ret

    def my_print(self):
        """Prints square"""
        print(self.my_sprint(), end="")

    def area(self):
        """Area of the new square
        Returns:
            The area
        """
        return self.__size ** 2
