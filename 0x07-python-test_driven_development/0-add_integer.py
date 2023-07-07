#!/usr/bin/python3


"""

This module adds two integers and returns sum of two numbers a & b.

Only accepts integers and floats else TypeError is raised

This module will convert float to integer

"""

def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a (int or float): First number
        b (int or float): Second number (default is 98)

    Returns:
        int: The addition of a and b

    Raises:
        TypeError: If a or b is not an integer or float

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)

