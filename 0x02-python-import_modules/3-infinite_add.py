#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    len_argv = len(argv)
    thissum = 0
    for i in range(1, len_argv):
        thissum += int(argv[i])
    print(thissum)
