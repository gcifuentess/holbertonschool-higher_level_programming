#!/usr/bin/python3
"""JSON module"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)."""

    encode = json.dumps(my_obj)
    return encode
