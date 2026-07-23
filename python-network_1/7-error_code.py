#!/usr/bin/python3
"""Module that takes in a URL, sends a request to it, and displays
the body of the response. If the HTTP status code is greater than or
equal to 400, it displays: Error code: <status code> instead.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
