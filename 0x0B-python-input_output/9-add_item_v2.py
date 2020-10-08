#!/usr/bin/python3
'''Module that adds all arguments to a Python list,
   and then save them to a file.
'''
import json
import sys
import os.path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


my_list = []
filename = "add_item.json"

if os.path.exists(filename):
    my_list = load_from_json_file(filename)

argv = sys.argv
for i in range(1, len(argv)):
    my_list.append(argv[i])

save_to_json_file(my_list, filename)
