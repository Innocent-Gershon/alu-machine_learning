#!/usr/bin/env python3
"""
Module for adding two 2D matrices element-wise.

This module provides the function `add_matrices2D`, which takes two
2D matrices and returns a new matrix containing the element-wise sum.
If the matrices are not the same shape, the function returns None.
"""

def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.

    Args:
        mat1 (list of lists): The first 2D matrix (ints or floats).
        mat2 (list of lists): The second 2D matrix (ints or floats).

    Returns:
        list of lists: A new 2D matrix representing the element-wise sum.
        None: If the matrices are not the same shape.
    """
    if len(mat1) != len(mat2) or any(len(r1) != len(r2) for r1, r2 in zip(mat1, mat2)):
        return None
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
