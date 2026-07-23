#!/usr/bin/python3
"""
Module that takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
Handles HTTPError exceptions.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
