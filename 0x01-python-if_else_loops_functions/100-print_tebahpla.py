#!/usr/bin/python3
for value in range(26, 0, -1):
    module = value % 2
    if module == 0:
        print("{:c}".format(value + 96), end="")
    else:
        print("{:c}".format(value + 64), end="")
