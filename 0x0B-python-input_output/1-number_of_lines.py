#!/usr/bin/python3
"""IO module"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file"""

    line_count = 0
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            line_count += 1
    return line_count
