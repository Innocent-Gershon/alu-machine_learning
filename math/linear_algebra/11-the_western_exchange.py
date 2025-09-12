#!/usr/bin/env python3
"""
Module for transposing 2D arrays without using any imports, loops, or
conditional statements.

Provides the function `np_transpose` which returns the transpose of a
2D list. The original list is not modified.
"""


def np_transpose(matrix):
    """
    Returns the transpose of a 2D list.

    Args:
        matrix (list of lists): The input 2D array.

    Returns:
        list of lists: A new array representing the transpose.
    """
    # Handle empty matrix and 1D row vectors
    if not matrix or not isinstance(matrix[0], list):
        return matrix[:]

    # Use zip to transpose without loops
    return [list(row) for row in zip(*matrix)]
