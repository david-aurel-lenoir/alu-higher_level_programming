#!/usr/bin/python3
"""Module that defines a function to print text with indentation.

This module provides the text_indentation function, which prints a
text adding 2 new lines after each ., ? and : character.
"""


def text_indentation(text):
    """Print a text with 2 new lines after ., ? and :.

    Args:
        text (str): the text to print.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    stripped = text.strip()
    line = ""
    for char in stripped:
        if char in "?.:":
            line += char
            print(line)
            print()
            line = ""
        elif char == " " and (len(line) == 0 or line[-1] == " "):
            continue
        else:
            line += char
    print(line, end="")
