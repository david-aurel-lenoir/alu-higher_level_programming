#!/usr/bin/python3
"""Module that prints the names defined in hidden_4.pyc"""
hidden_4 = __import__("hidden_4")


if __name__ == "__main__":
    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)
