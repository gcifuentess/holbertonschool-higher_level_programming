#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        module = ((number * -1) % 10)
    else:
        module = number % 10
    print(module, end="")
    return module
