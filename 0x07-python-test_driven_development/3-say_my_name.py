#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor and rounds the result to 2 decimal places.

    Args:
        matrix (list of lists): A matrix (list of lists) containing integers or floats.
        div (int or float): The divisor to divide all elements of the matrix.

    Returns:
        list of lists: A new matrix with all elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to zero.
    """
    errorMessage = "matrix must be a matrix (list of lists) of integers/floats"
    
    # Check if matrix is a valid matrix (non-empty list of lists of integers/floats)
    if not matrix or not isinstance(matrix, list):
        raise TypeError(errorMessage)
    
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(errorMessage)
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError(errorMessage)
        if len(row) == 0:
            raise TypeError(errorMessage)
    
    # Ensure all rows are of the same length
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a valid number and non-zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div and round to 2 decimal places
    return [[round(item / div, 2) for item in row] for row in matrix]

