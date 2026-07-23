#!/usr/bin/python3
"""
Module that takes in a URL, sends a request, and displays
the value of the X-Request-Id variable in the response header.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header_value = response.headers.get("X-Request-Id")
        print(header_value)
