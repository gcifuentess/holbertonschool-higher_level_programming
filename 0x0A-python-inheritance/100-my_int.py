#!/usr/bin/python3
"""int rebel module"""


class MyInt(int):
    """MyInt int subclass"""

    def __eq__(self, other):
        """eq override"""
        return int(self) != int(other)

    def __ne__(self, other):
        """ne override"""
        return int(self) == int(other)
