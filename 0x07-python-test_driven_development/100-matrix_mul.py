#!/usr/bin/python3
"""Matrix multiplication (two matrices)
"""


def matrix_mul(m_a, m_b):
    """Function to multiply two matrices and return the resulting matrix
    """

    
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    row_size = len(m_a[0])
    if not all(len(row) == row_size for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    col_size = len(m_b[0])
    if not all(len(row) == col_size for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    
    if row_size != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                sum += m_a[i][k] * m_b[k][j]
            row.append(sum)
        result.append(row)

    return result
