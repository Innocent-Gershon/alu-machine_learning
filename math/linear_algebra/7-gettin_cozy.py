#!/usr/bin/env python3
"""
Module for concatenating two 2D matrices along a specific axis.

Provides the function `cat_matrices2D` which concatenates two matrices
either row-wise (axis=0) or column-wise (axis=1) and returns a new matrix.
If the matrices cannot be concatenated, the function returns None.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along a given axis.

    Args:
        mat1 (list of lists): First 2D matrix (ints/floats).
        mat2 (list of lists): Second 2D matrix (ints/floats).
        axis (int): 0 for row-wise, 1 for column-wise concatenation.

    Returns:
        list of lists: New matrix after concatenation.
        None: If matrices cannot be concatenated.
    """
    # Row-wise concatenation
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    # Column-wise concatenation
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1[:] + row2[:] for row1, row2 in zip(mat1, mat2)]

    # Invalid axis
    else:
        return None
