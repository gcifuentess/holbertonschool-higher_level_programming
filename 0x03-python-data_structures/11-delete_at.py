#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list:
        return None
    new_list = []
    for i in range(0, len(my_list)):
        if idx != i:
            new_list.append(my_list[i])
    return new_list
