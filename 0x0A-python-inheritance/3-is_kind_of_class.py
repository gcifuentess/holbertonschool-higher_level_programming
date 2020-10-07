#!/usr/bin/python3
"""is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance
       of the specified class.
    Args:
        obj: object.
        a_class: the class to compare with.
    Return:
        True or False.
    """
    return isinstance(obj, a_class)
