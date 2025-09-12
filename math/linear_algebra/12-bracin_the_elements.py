#!/usr/bin/env python3
"""
Element-wise operations on numpy arrays with broadcasting.
"""

import numpy as np

def np_elementwise(mat1, mat2):
    add = mat1 + mat2
    sub = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2
    return add, sub, mul, div
