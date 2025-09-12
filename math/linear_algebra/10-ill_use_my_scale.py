#!/usr/bin/env python3
"""
Module for calculating the shape of a NumPy array.

Provides the function `np_shape` which returns the shape of a
numpy.ndarray as a tuple of integers.
"""


def np_shape(matrix):
    """
    Returns the shape of a NumPy ndarray.

    Args:
        matrix (numpy.ndarray): The input array.

    Returns:
        tuple: Shape of the array as a tuple of integers.
    """
    return matrix.shape
