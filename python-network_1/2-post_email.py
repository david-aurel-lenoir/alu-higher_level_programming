#!/usr/bin/python3
"""
Module that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8).
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Préparation des données pour la requête POST
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')

    # Création et envoi de la requête
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(body)
