#!/usr/bin/python3
"""IO module"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the
       number of characters written.
    """
    num_char = 0
    with open(filename, mode='w', encoding='utf-8') as a_file:
        num_char = a_file.write(text)
    return num_char
