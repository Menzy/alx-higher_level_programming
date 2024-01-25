#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a copy of the input matrix to avoid modifying the original
    n_matrix = matrix[:]

    # Iterate over each row in the matrix
    for i in range(len(n_matrix)):
        # Square each element in the current row
        n_matrix[i] = list(map(lambda x: x**2, n_matrix[i]))

    # Return the modified matrix with all elements squared
    return n_matrix
