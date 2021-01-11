#!/usr/bin/python3
'''urllib module'''
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    data = parse.urlencode(values).encode()
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        request = response.read().decode('utf8')
    print(request)
