#!/usr/bin/python3
'''urllib module'''
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        request = response.read()
        headers = response.info()
    print(headers['X-Request-Id'])
