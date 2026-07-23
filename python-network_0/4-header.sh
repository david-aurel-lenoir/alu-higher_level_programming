#!/bin/bash
# Takes in a URL, sends a GET request with a header variable, and displays the response
curl -s -H "X-School-User-Id: 98" "$1"
