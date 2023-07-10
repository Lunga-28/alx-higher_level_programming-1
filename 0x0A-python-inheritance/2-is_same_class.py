#!/usr/bin/python3
"""
contains a function that returns
True if the obj is exactly an instance of the
specified class elsere turns False
"""

def is_same_class(obj, a_class):
    """
    checks for object
    """
    return (type(obj) == a_class)
