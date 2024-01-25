#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    # Check if the input matrix is empty
    if not matrix:
        return []

    # Use nested map to square each element in the matrix
    squared_matrix = list(
        map(lambda row: list(map(lambda x: x ** 2, row)), matrix)
    )

    return squared_matrix
