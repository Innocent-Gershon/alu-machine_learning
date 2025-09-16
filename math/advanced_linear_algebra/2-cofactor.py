#!/usr/bin/env python3
"""Cofactor matrix calculation
"""


def cofactor(matrix):
    """Calculates the cofactor matrix of a square matrix.

    Args:
        matrix (list of lists): matrix to evaluate.

    Returns:
        list of lists: the cofactor matrix.

    Raises:
        TypeError: if matrix is not a list of lists.
        ValueError: if matrix is not square or is empty.
    """
    # Validate matrix type
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError("matrix must be a list of lists")

    if matrix == []:
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    # Ensure non-empty square
    if n == 0 or not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # Special case for 1x1 matrix
    if n == 1:
        return [[1]]

    def determinant(mat):
        """Helper to calculate determinant recursively."""
        size = len(mat)
        if size == 1:
            return mat[0][0]
        if size == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        det = 0
        for col in range(size):
            submatrix = [
                r[:col] + r[col + 1:]
                for k, r in enumerate(mat)
                if k != 0
            ]
            det += ((-1) ** col) * mat[0][col] * determinant(submatrix)
        return det

    # Build the cofactor matrix
    cof = []
    for i in range(n):
        row_cof = []
        for j in range(n):
            submatrix = [
                r[:j] + r[j + 1:]
                for k, r in enumerate(matrix)
                if k != i
            ]
            value = determinant(submatrix)
            row_cof.append(((-1) ** (i + j)) * value)
        cof.append(row_cof)

    return cof
