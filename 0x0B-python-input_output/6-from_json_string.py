#!/usr/bin/python3
"""JSON module"""
import json


def from_json_string(my_str):
    """Returns the JSON representation of an object (string)."""

    decode = json.loads(my_str)
    return decode
