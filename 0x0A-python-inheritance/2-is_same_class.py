#!/usr/bin/python3
"""is_same_class module"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance
       of the specified class.
    Args:
        obj: object.
        a_class: the class to compare with.
    Return:
        True or False.
    """
    return type(obj) == a_class
