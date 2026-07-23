#!/usr/bin/python3
"""Module that takes GitHub credentials (username and personal access
token as password) and uses the GitHub API with Basic Authentication
to display the id of the authenticated user.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    print(response.json().get("id"))
