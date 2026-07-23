#!/bin/bash
# Takes in a URL, sends a request, and displays the body size in bytes
curl -s "$1" | wc -c
