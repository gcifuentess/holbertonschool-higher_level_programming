#!/usr/bin/python3
"""MyList Module"""


class MyList(list):
    """My List Class
    Parent Class: list
    """
    def print_sorted(self):
        """prints the list ascending sorted"""
        print(sorted(self))
