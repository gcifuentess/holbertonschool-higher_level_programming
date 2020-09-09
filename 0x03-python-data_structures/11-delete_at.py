#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    len_l = len(my_list)
    if idx < len_l and abs(idx) <= len_l:
            del my_list[idx]
    return my_list
