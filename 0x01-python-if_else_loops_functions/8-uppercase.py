#!/usr/bin/python3
def uppercase(str):
    """prints a string in uppercase followed by a new line"""
    for tchar in str:
        value = ord(tchar)
        if value in range(97, 123):
            value = value - 32
        print("{:c}".format(value), end="")
    print("")
