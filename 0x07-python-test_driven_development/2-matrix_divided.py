def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number

    Args:
        matrix (list): List of lists containing integers or floats
        div (int or float): Number to divide the matrix elements by

    Returns:
        list: A new matrix with elements divided by div, rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats
        TypeError: If each row of the matrix does not have the same size
        TypeError: If div is not a number (integer or float)
        ZeroDivisionError: If div is equal to 0

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
