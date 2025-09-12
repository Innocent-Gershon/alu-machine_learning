#!/usr/bin/env python3
"""
Module for performing matrix multiplication.

Provides the function `mat_mul` which multiplies two 2D matrices
and returns a new matrix. If the matrices cannot be multiplied,
the function returns None.
"""


def mat_mul(mat1, mat2):
    """
    Performs matrix multiplication of two 2D matrices.

    Args:
        mat1 (list of lists): First matrix (ints/floats).
        mat2 (list of lists): Second matrix (ints/floats).

    Returns:
        list of lists: New matrix representing the product of mat1 and mat2.
        None: If the matrices cannot be multiplied.
    """
    # Number of columns in mat1 must equal number of rows in mat2
    if len(mat1[0]) != len(mat2):
        return None

    # Initialize result matrix with zeros
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

    # Perform multiplication
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
