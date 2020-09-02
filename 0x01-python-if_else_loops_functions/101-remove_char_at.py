#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = ""
    i = 0
    for tchar in str:
        if i != n:
            strcpy = strcpy + tchar
        i += 1
    return (strcpy)
