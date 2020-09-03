#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    argv_len = len(argv) - 1
    if argv_len == 1:
        print("1 argument:")
    elif argv_len == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(argv_len))

    i = 0
    for argument in argv:
        if i > 0:
            print("{}: {}".format(i, argument))
        i += 1
