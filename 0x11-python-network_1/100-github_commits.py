#!/usr/bin/python3
'''request module'''
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/repos/' +\
          argv[2] + '/' + argv[1] + '/commits'
    header = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, header)
    r = r.json()
    commits = 10
    for commit in r:
        if commits > 0:
            commits -= 1
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
        else:
            break
