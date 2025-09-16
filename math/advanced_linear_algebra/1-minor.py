#!/usr/bin/env python3
"""Minor matrix calculation
"""

from 0-determinant import determinant


def minor(matrix):
    """Calculates the minor matrix of a square matrix.

    Args:
        matrix (list of lists): matrix to evaluate.

    Returns:
        list of lists: the minor matrix.

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

    minors = []
    for i in range(n):
        row_minors = []
        for j in range(n):
            # Build submatrix by removing row i and column j
            submatrix = [
                r[:j] + r[j + 1:]
                for k, r in enumerate(matrix)
                if k != i
            ]
            row_minors.append(determinant(submatrix))
        minors.append(row_minors)

    return minors
