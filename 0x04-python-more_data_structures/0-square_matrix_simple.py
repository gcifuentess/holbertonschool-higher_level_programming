#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_s = []
    for i in range(0, len(matrix)):
        matrix_s.append(list(map(lambda x: x ** 2, matrix[i])))
    return matrix_s
