#!/usr/bin/python3
"""Module that takes in a URL, sends a request to it, and displays
the value of the X-Request-Id variable found in the response header.
"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
