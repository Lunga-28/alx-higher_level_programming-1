#!/usr/bin/python3
"""
sends a request to url
then displays the value of X-Request-Id variable
"""
import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        pass
    print(response.headers.get('X-Request-Id'))
