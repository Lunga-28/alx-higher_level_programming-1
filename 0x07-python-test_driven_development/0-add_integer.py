#!/usr/bin/python3

"""

adds two integers and returns sum of two numbers a & b.

accepts integers and floats else TypeError is raised

convert float to integer

"""

def add_integer(a, b=98):


    if isinstance(a, (int, float)) is False:

        raise TypeError('a must be an integer')

    elif isinstance(b, (int, float)) is False:

        raise TypeError('b must be an integer')

    return(int(a) + int(b))
