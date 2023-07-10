#!/usr/bin/python3
"""
contains a class
that inherits from int
"""

class MyInt(int):
    """
    opposite to == and !=
    """
    def __eq__(self, other):
        """
        returns opposite of ==
        """
        return (not super().__eq__(other))

    def __ne__(self, other):
        """
        returns opposite of not !=
        """
        return (not super().__ne__(other))
