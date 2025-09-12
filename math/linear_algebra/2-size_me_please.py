#!/usr/bin/env python3
"""
Module for calculating the shape of a matrix.

This module contains the function `matrix_shape` which determines
the dimensions of a matrix and returns them as a list of integers.
"""


def matrix_shape(matrix):
    """
    Calculates the shape (dimensions) of a matrix.

    Args:
        matrix (list): A nested list representing the matrix.

    Returns:
        list: A list of integers representing the size of each dimension.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
