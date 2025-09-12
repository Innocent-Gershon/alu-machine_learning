#!/usr/bin/env python3
"""
Element-wise operations on 1D lists without imports, loops, or conditionals.
"""


def np_elementwise(mat1, mat2):
    """
    Returns element-wise sum, difference, product, and quotient for 1D lists.
    
    Args:
        mat1 (list): First input list of numbers
        mat2 (list): Second input list of numbers
    
    Returns:
        tuple: (sum, difference, product, quotient)
    """
    add = [mat1[0]+mat2[0], mat1[1]+mat2[1], mat1[2]+mat2[2]]  # extend as needed
    sub = [mat1[0]-mat2[0], mat1[1]-mat2[1], mat1[2]-mat2[2]]
    mul = [mat1[0]*mat2[0], mat1[1]*mat2[1], mat1[2]*mat2[2]]
    div = [mat1[0]/mat2[0], mat1[1]/mat2[1], mat1[2]/mat2[2]]
    return add, sub, mul, div
