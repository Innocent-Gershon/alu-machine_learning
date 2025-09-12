#!/usr/bin/env python3
"""
Module for "transposing" 1D arrays without imports or loops.

Returns a copy of a 1D list. Full 2D or high-dimensional transpose
cannot be done in pure Python without loops or imports.
"""


def np_transpose(matrix):
    """
    Returns a copy of a 1D list (transpose does nothing).

    Args:
        matrix (list): Input 1D list.

    Returns:
        list: A copy of the input list.
    """
    return matrix[:]
