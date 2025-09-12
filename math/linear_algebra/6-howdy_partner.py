#!/usr/bin/env python3
"""
Module for concatenating two arrays.

This module provides the function `cat_arrays` which takes two arrays
(lists of numbers) and returns a new list containing all elements
from the first array followed by all elements from the second array.
"""


def cat_arrays(arr1, arr2):
    """
    Concatenates two arrays into a new list.

    Args:
        arr1 (list): The first array (list of ints or floats).
        arr2 (list): The second array (list of ints or floats).

    Returns:
        list: A new list containing all elements from arr1 followed
              by all elements from arr2.
    """
    return arr1 + arr2
