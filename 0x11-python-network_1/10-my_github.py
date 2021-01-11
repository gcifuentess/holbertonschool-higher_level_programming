#!/usr/bin/python3
'''request module'''
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    r = r.json()
    try:
        print(r['id'])
    except KeyError:
        print("None")
