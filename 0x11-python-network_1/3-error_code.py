#!/usr/bin/python3
'''urllib module'''
from urllib import request, parse, error
from sys import argv


if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            request = response.read().decode('utf8')
        print(request)
    except error.HTTPError as e:
        print("Error code:", e.code)
