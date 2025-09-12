#!/usr/bin/env python3
"""
Module for transposing a NumPy array.

Provides the function `np_transpose` which returns the transpose of
a numpy.ndarray. The original array is not modified.
"""


import numpy as np

def np_transpose(matrix):
    """
    Returns the transpose of a numpy.ndarray.

    Args:
        matrix (numpy.ndarray): The input array.

    Returns:
        numpy.ndarray: A new array representing the transpose of the input.
    """
    return np.transpose(matrix)
