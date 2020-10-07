#!/usr/bin/python3
"""IO module"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and returns the
       number of characters added.
    """

    num_char = 0
    with open(filename, mode='a', encoding='utf-8') as a_file:
        num_char = a_file.write(text)
    return num_char
