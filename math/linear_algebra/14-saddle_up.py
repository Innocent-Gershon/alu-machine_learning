#!/usr/bin/env python3
"""
Performs matrix multiplication using numpy.
"""


import numpy as np


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication of two numpy arrays.

    Args:
        mat1 (np.ndarray): First input matrix.
        mat2 (np.ndarray): Second input matrix.

    Returns:
        np.ndarray: Result of mat1 @ mat2 (matrix multiplication).
    """
    return np.matmul(mat1, mat2)
