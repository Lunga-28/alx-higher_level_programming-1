#!/usr/bin/python3
"""
a function that adds new attribute
"""

def add_attribute(ob, attr, value):
    """
    add attribute to class or raises error
    """
    if hasattr(ob, "__dict__"):
        setattr(ob, attr, value)
    else:
        raise TypeError("can't add new attribute")
