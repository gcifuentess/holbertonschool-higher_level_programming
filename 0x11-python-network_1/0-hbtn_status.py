#!/usr/bin/python3
'''urllib module'''
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        request = response.read()

        request_utf8 = request.decode('utf8')
        print("Body response:\n \
\t- type: {}\n \
\t- content: {}\n \
\t- utf8 content: {}".format(type(request), request, request_utf8))
