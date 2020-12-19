#!/usr/bin/python3
"""find-peak algorithm module"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""

    if list_of_integers:
        list_i = list_of_integers
        len_i = len(list_i)
        if len_i > 2:
            pivot = int(len_i / 2)
            peak = list_i[pivot]
            if peak > list_i[pivot - 1] and peak > list_i[pivot + 1]:
                return peak
            elif peak > list_i[pivot + 1]:
                return find_peak(list_i[:pivot])
            else:
                return find_peak(list_i[pivot + 1:])
        else:
            return max(list_i)
    else:
        return None
