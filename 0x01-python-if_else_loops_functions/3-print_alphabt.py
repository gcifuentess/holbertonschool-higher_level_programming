#!/usr/bin/python3
for lowercase in range(97, 123):
    if (lowercase in [101, 113]):
        continue
    else:
        print("{:c}".format(lowercase), end="")
