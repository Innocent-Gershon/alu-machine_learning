#!/usr/bin/env python3
"""
Module for transposing a 2D array without using any imports.

Provides the function `np_transpose` which returns the transpose
of a 2D list or list of lists. The original array is not modified.
"""


def np_transpose(matrix):
    """
    Returns the transpose of a 2D list.

    Args:
        matrix (list of lists): The input 2D array.

    Returns:
        list of lists: A new array representing the transpose.
    """
    if not matrix:  # Handle empty list
        return []
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
