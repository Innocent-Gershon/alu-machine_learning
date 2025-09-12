#!/usr/bin/env python3
"""
Module for performing element-wise arithmetic on numpy arrays.

Provides the function `np_elementwise` which returns the element-wise
sum, difference, product, and quotient of two arrays or an array and a scalar.
No loops or conditionals are used.
"""


import numpy as np

def np_elementwise(mat1, mat2):
    """
    Perform element-wise addition, subtraction, multiplication, and division.

    Args:
        mat1 (numpy.ndarray): First input array.
        mat2 (numpy.ndarray or scalar): Second input array or scalar.

    Returns:
        tuple: A tuple containing element-wise sum, difference,
               product, and quotient, respectively.
    """
    add = mat1 + mat2
    sub = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2
    return add, sub, mul, div
