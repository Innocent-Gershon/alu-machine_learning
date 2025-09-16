#!/usr/bin/env python3
"""Determinant calculation
"""


def determinant(matrix):
    """Calculates the determinant of a matrix.

    Args:
        matrix (list of lists): matrix to evaluate.

    Returns:
        int/float: determinant of matrix.

    Raises:
        TypeError: if matrix is not a list of lists.
        ValueError: if matrix is not square.
    """
    # Validate matrix type
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError("matrix must be a list of lists")

    # Empty matrix (like [])
    if matrix == []:
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    # Handle 0x0 matrix: [[]]
    if n == 1 and matrix[0] == []:
        return 1

    # Ensure square
    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base cases
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive Laplace expansion (first row)
    det = 0
    for col in range(n):
        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)
    return det
