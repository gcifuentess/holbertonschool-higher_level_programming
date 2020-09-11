#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_keys = sorted(a_dictionary.keys())
    for a_key in a_keys:
        print("{}: {}".format(a_key, a_dictionary[a_key]))
