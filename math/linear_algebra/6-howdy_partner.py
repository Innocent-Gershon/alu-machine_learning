#!/usr/bin/env python3
"""
Module for concatenating two arrays.

Provides the function `cat_arrays` which returns a new list containing
all elements of arr1 followed by all elements of arr2.
"""


def cat_arrays(arr1, arr2):
    """
    Concatenates two arrays into a new list.

    Args:
        arr1 (list): First array of ints/floats.
        arr2 (list): Second array of ints/floats.

    Returns:
        list: A new list containing elements of arr1 then arr2.
    """
    return arr1 + arr2
