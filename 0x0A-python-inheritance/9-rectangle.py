#!/usr/bin/python3
"""Rectangle Module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle subclass"""

    def __init__(self, width, height):
        """Rectangle Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def __str__(self):
        """string to print"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
