#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """list of available attributes and methods of an object.
    Args:
        obj: object.
    Return:
        the list of attributes and methods.
    """
    members = list(dir(obj))
    return members
