#!/usr/bin/env python3
"""
Concatenates two numpy matrices along a specified axis.
"""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two numpy matrices along a given axis.

    Args:
        mat1 (np.ndarray): First input matrix.
        mat2 (np.ndarray): Second input matrix.
        axis (int, optional): Axis along which to concatenate. Defaults to 0.

    Returns:
        np.ndarray: New matrix resulting from concatenation.
    """
    return np.concatenate((mat1, mat2), axis=axis)
