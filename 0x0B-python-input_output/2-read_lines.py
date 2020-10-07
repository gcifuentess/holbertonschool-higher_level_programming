#!/usr/bin/python3
"""IO module"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file (UTF8) and prints it to stdout"""

    lines_count = 0
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            lines_count += 1
            if lines_count <= nb_lines or nb_lines <= 0:
                print(line, end='')
            else:
                break
