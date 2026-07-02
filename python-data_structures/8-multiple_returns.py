#!/usr/bin/python3
"""Module that returns the length of a string and its first character."""


def multiple_returns(sentence):
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]

    return (len(sentence), first_char)
