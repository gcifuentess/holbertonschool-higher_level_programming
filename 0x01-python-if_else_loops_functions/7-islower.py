#!/usr/bin/python3
def islower(c):
    """checks for lowercase character
    Returns True if c is lowercase
    Returns False otherwise
    """
    ascii_code = ord(c)
    if ascii_code in range(97, 123):
        return True
    else:
        return False
