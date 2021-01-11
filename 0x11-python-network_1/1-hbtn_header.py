#!/usr/bin/python3
'''urllib module'''
import urllib.request
from sys import argv


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        headers = response.info()
    print(headers['X-Request-Id'])
