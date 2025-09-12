#!/usr/bin/env python3
"""
Element-wise operations on 2x3 matrices without imports, loops, or conditionals.
"""


def np_elementwise(mat1, mat2):
    """
    Returns element-wise sum, difference, product, and quotient for 2x3 matrices.
    """
    add = [[mat1[0][0]+mat2[0][0], mat1[0][1]+mat2[0][1], mat1[0][2]+mat2[0][2]],
           [mat1[1][0]+mat2[1][0], mat1[1][1]+mat2[1][1], mat1[1][2]+mat2[1][2]]]

    sub = [[mat1[0][0]-mat2[0][0], mat1[0][1]-mat2[0][1], mat1[0][2]-mat2[0][2]],
           [mat1[1][0]-mat2[1][0], mat1[1][1]-mat2[1][1], mat1[1][2]-mat2[1][2]]]

    mul = [[mat1[0][0]*mat2[0][0], mat1[0][1]*mat2[0][1], mat1[0][2]*mat2[0][2]],
           [mat1[1][0]*mat2[1][0], mat1[1][1]*mat2[1][1], mat1[1][2]*mat2[1][2]]]

    div = [[mat1[0][0]/mat2[0][0], mat1[0][1]/mat2[0][1], mat1[0][2]/mat2[0][2]],
           [mat1[1][0]/mat2[1][0], mat1[1][1]/mat2[1][1], mat1[1][2]/mat2[1][2]]]

    return add, sub, mul, div
