#!/usr/bin/python3
'''request module'''
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        values = {'q': argv[1]}
    else:
        values = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data=values)
    try:
        request = r.json()
        if request != {}:
            print("[{}] {}".format(request['id'], request['name']))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
