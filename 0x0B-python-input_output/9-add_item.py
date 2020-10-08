#!/usr/bin/python3
"""JSON module"""
import json
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


def class_to_json(obj):
    """Adds all arguments to a Python list, and then save them to a file"""

    filename = 'add_item.json'
    with open(filename, mode='a', encoding='utf-8') as a_file:
        a_file.write('')

    with open(filename, mode='r', encoding='utf-8') as a_file:
        line = a_file.readline()

    if line != '':
        new_object = load_from_json_file(filename)
    else:
        new_object = []
    if obj != "do not include":
        new_object.append(obj)
    save_to_json_file(new_object, filename)


if __name__ == "__main__":
    import sys

    argv = sys.argv
    argv_len = len(argv)

    i = 0
    for arg in argv:
        if i > 0:
            class_to_json(arg)
        else:
            class_to_json("do not include")
        i += 1
