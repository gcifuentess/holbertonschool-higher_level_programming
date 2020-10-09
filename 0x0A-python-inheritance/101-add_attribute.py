#!/usr/bin/python3
"""Add atribute module"""


def add_attribute(obj, att, value):
    '''function to add attribute if it is possible'''
    if (hasattr(obj, "__dict__") or
        (hasattr(obj, "__slots__") and
         att in obj.__slots__)):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")
