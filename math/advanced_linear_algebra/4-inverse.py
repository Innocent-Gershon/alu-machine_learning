#!/usr/bin/env python3
"""Calculate the inverse of a matrix without imports"""


def determinant(matrix):
    """Calculate determinant of a matrix"""
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (matrix[0][0] * matrix[1][1] -
                matrix[0][1] * matrix[1][0])

    det = 0
    for c in range(n):
        sub = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(sub)
    return det


def adjugate(matrix):
    """Calculate adjugate of a matrix"""
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)

    if n == 1:
        return [[1]]

    cofactors = []
    for r in range(n):
        cofactor_row = []
        for c in range(n):
            sub = [row[:c] + row[c+1:]
                   for i, row in enumerate(matrix) if i != r]
            sign = (-1) ** (r + c)
            cofactor_row.append(sign * determinant(sub))
        cofactors.append(cofactor_row)

    # transpose
    return [[cofactors[j][i] for j in range(n)] for i in range(n)]


def inverse(matrix):
    """Calculate inverse of a matrix"""
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")

    det = determinant(matrix)
    if det == 0:
        return None

    adj = adjugate(matrix)
    return [[elem / det for elem in row] for row in adj]
