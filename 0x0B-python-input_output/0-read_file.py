#!/usr/bin/python3
"""IO module"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            print(line, end='')
