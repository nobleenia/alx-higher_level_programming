#!/usr/bin/python3
"""
This module finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers
    """
    if bool(list_of_integers) is False:
        return None
    list_of_integers.sort()
    peak_int = list_of_integers[-1]

    return peak_int
