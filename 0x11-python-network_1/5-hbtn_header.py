#!/usr/bin/python3
'''request module'''
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    request = r.headers.get('X-Request-Id')
    print(request)
