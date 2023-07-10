#!/usr/bin/python3
"""
contains a function that returns
the list of available attributes
and methods
"""


def lookup(obj):
    """
    returns the list of available
    attributes and methods
    """
    return (dir(obj))
