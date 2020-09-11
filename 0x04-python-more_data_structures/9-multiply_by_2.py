#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys_a = a_dictionary.keys()
    new_dic = {}
    for key in keys_a:
        new_dic[key] = a_dictionary[key] * 2
    return new_dic
