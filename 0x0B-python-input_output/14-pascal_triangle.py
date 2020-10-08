#!/usr/bin/python3
"""Pascal Triangle module"""


def pascal_triangle(n):
    """builds a pascal matrix"""

    pascal = []
    if n > 0:
        for i in range(n):
            row = []
            row.append(1)
            j = 0
            while j < (i - 1):
                row.append(pascal[i - 1][j] + pascal[i - 1][j + 1])
                j += 1
            if i != 0:
                row.append(1)
            pascal.append(row)
    return pascal
