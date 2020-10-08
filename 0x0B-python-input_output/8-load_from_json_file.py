#!/usr/bin/python3
"""JSON module"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""

    with open(filename, encoding='utf-8') as a_file:
        line = a_file.readline()
        new_object = json.loads(line)
    return new_object
