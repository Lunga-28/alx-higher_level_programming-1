#!/usr/bin/python3
"""
contains a function that returns
True if the object is an instance of a class
that is inherited from the specified class
otherwise returns False.
"""


def inherits_from(obj, a_class):
    """
    returns True or False
    """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
