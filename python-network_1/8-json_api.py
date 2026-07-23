#!/usr/bin/python3
"""Module that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter,
then displays the result based on the JSON response received.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": letter})
    try:
        result = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not result:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
