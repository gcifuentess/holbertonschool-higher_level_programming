#!/usr/bin/python3
"""Geometry Module"""


class BaseGeometry():
    """Base Geometry Constructor"""

    def area(self):
        """Raises Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
