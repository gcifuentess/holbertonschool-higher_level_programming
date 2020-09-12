#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    my_dicc = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum, i, b = 0, 0, 0
    while i < len(roman_string):
        a = my_dicc[roman_string[i]]
        if i != len(roman_string) - 1:
            b = my_dicc[roman_string[i + 1]]
        if a < b:
            sum += (b - a)
            i += 1
        else:
            sum += a
        i += 1
    return sum
