#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        max_score = 0
        keys_a = a_dictionary.keys()
        for key in keys_a:
            if a_dictionary[key] >= max_score:
                max_score = a_dictionary[key]
                max_key = key
    return max_key
