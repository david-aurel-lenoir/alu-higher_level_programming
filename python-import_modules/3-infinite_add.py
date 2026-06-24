#!/usr/bin/python3
"""Module that prints the sum of all arguments passed to it."""
from sys import argv


if __name__ == "__main__":
    total = 0
    for i in range(1, len(argv)):
        total += int(argv[i])
    print(total)
