#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix where each number is squared
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: x ** 2, row)))
    return new_matrix

