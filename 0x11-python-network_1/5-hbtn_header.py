#!/usr/bin/python3
"""
takes in a url to send a request to the url
"""
import requests
from sys import argv

if __name__ == "__main__":
    reply = requests.get(argv[1])
    print(reply.headers.get('X-Request-Id'))
