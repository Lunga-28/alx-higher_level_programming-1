#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
   
    result = [[0 for _ in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Compute the square value of each element and store it in the result matrix
            result[i][j] = matrix[i][j] ** 2

    return result
