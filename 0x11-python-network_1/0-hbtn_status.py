#!/usr/bin/python3
'''urllib module'''
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        request = response.read()
    request_utf8 = request.decode('utf8')
    print("Body response:")
    print("\t- type: {}".format(type(request)))
    print("\t- content: {}".format(request))
    print("\t- utf8 content: {}".format(request_utf8))
