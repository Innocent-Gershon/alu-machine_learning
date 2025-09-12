#!/usr/bin/env python3
"""
Element-wise operations on fixed-size lists without imports, loops, or conditionals.
"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division
    on fixed-size 1D or 2D lists. Returns a tuple of four lists/matrices.
    
    Args:
        mat1 (list): First input list or matrix
        mat2 (list): Second input list or matrix (same shape as mat1)
    
    Returns:
        tuple: (add, sub, mul, div)
    """
    # Example: for 2x3 2D lists
    add = [[mat1[0][0]+mat2[0][0], mat1[0][1]+mat2[0][1], mat1[0][2]+mat2[0][2]],
           [mat1[1][0]+mat2[1][0], mat1[1][1]+mat2[1][1], mat1[1][2]+mat2[1][2]]]

    sub = [[mat1[0][0]-mat2[0][0], mat1[0][1]-mat2[0][1], mat1[0][2]-mat2[0][2]],
           [mat1[1][0]-mat2[1][0], mat1[1][1]-mat2[1][1], mat1[1][2]-mat2[1][2]]]

    mul = [[mat1[0][0]*mat2[0][0], mat1[0][1]*mat2[0][1], mat1[0][2]*mat2[0][2]],
           [mat1[1][0]*mat2[1][0], mat1[1][1]*mat2[1][1], mat1[1][2]*mat2[1][2]]]

    div = [[mat1[0][0]/mat2[0][0], mat1[0][1]/mat2[0][1], mat1[0][2]/mat2[0][2]],
           [mat1[1][0]/mat2[1][0], mat1[1][1]/mat2[1][1], mat1[1][2]/mat2[1][2]]]

    return add, sub, mul, div
