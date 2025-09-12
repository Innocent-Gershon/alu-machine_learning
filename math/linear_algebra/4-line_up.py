#!/usr/bin/env python3
"""
Module for adding two arrays element-wise.

This module provides the function `add_arrays`, which takes two
arrays (lists of numbers) and returns a new array containing the
element-wise sum. If the two arrays are not the same length, the
function returns None.
"""

def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Args:
        arr1 (list): The first array (list of ints or floats).
        arr2 (list): The second array (list of ints or floats).

    Returns:
        list: A new list containing the element-wise sum of arr1 and arr2.
        None: If the arrays are not the same length.
    """
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
