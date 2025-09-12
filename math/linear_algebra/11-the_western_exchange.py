#!/usr/bin/env python3
"""
Module for transposing numpy arrays.

Provides the function `np_transpose` which returns the transpose of
a numpy.ndarray. Works for 1D, 2D, and higher-dimensional arrays.
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
