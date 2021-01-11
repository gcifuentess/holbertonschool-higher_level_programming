#!/usr/bin/python3
'''request module'''
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    request = r.text
    print("Body response:")
    print("\t- type: {}".format(type(request)))
    print("\t- content: {}".format(request))
