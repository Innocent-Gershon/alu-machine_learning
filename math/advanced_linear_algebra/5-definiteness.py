#!/usr/bin/env python3
"""Calculate definiteness of a matrix"""
import numpy as np


def definiteness(matrix):
    """Calculates the definiteness of a matrix"""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return None

    if matrix.size == 0:
        return None

    # Check if matrix is symmetric (required for definiteness)
    if not np.allclose(matrix, matrix.T):
        return None

    # Compute eigenvalues
    eigenvalues = np.linalg.eigvals(matrix)

    if np.all(eigenvalues > 0):
        return "Positive definite"
    elif np.all(eigenvalues >= 0):
        return "Positive semi-definite"
    elif np.all(eigenvalues < 0):
        return "Negative definite"
    elif np.all(eigenvalues <= 0):
        return "Negative semi-definite"
    elif np.any(eigenvalues > 0) and np.any(eigenvalues < 0):
        return "Indefinite"

    return None
