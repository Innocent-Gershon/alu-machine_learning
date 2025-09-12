#!/usr/bin/env python3
"""
Module for extracting a 2D plane from a 3D matrix.

This module provides the function `extract_plane`, which takes a 3D
matrix and an index, then returns the 2D plane at that index.
"""


def extract_plane(matrix, plane_index):
    """
    Extracts a 2D plane from a 3D matrix.

    Args:
        matrix (list of lists of lists): The 3D matrix.
        plane_index (int): Index of the plane to extract.

    Returns:
        list of lists: The 2D plane at the given index.
        None: If the plane_index is out of range.
    """
    if plane_index < 0 or plane_index >= len(matrix):
        return None
    return [row[:] for row in matrix[plane_index]]


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.

    Args:
        mat1 (list of lists): First 2D matrix (ints or floats).
        mat2 (list of lists): Second 2D matrix (ints or floats).

    Returns:
        list of lists: New matrix representing element-wise sum.
        None: If matrices are not the same shape.
    """
    if len(mat1) != len(mat2) or any(
        len(r1) != len(r2) for r1, r2 in zip(mat1, mat2)
    ):
        return None
    return [
        [mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]
        for i in range(len(mat1))
    ]


def transpose_matrix(matrix):
    """
    Returns the transpose of a 2D matrix.

    Args:
        matrix (list of lists): The 2D matrix to transpose.

    Returns:
        list of lists: New matrix representing the transpose.
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


if __name__ == "__main__":
    mat3d = [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
        [[9, 10], [11, 12]]
    ]
    print("Plane at index 1:", extract_plane(mat3d, 1))

    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    print("Sum of matrices:", add_matrices2D(mat1, mat2))

    print("Transpose of mat1:", transpose_matrix(mat1))
