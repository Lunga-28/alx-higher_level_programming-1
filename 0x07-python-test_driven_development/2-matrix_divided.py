#!/usr/bin/python3

"""

This module defines function to divide two list int a matrix

"""


def matrix_divided(matrix, div):
    """

    Divides list and Raises TypeError

    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    type_err = "matrix must be a matrix (list of lists) of integers/floats"
    size_err = "Each row of the matrix must have the same size"

    new_matrix = []

    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(type_err)

    old_size = len(matrix[0])

    for count, row in enumerate(matrix):
        if not isinstance(row, list):
            raise TypeError(type_err)

        if len(row) != old_size:
            raise TypeError(size_err)

        old_size = len(row)
        new_row = row[:]
        
        for i, item in enumerate(row):
            if not isinstance(item, (int, float)):
                raise TypeError(type_err)
            
            new_row[i] = round(item / div, 2)

        new_matrix.append(new_row)

    return new_matrix
