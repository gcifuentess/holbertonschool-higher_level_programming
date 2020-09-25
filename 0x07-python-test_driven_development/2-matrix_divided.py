#!/usr/bin/python3
"""matrix_divided module"""


def matrix_divided(matrix, div):
    """Matrix division

    Args:
        matrix: matrix containing int or float
        div: integer or float to divide the matrix

    Returns:
        list: divided matrix

    Raises:
        TypeError: When matrix is not containing int or float
        TypeError: When each row of the matrix are not all same size
        TypeError: If div is not int or float
        ZeroDivisionError: When div is zero
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        + "integers/floats")
    for row in matrix:
        if type(matrix) is not list or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of "
                            + "integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if type(x) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                + "integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
