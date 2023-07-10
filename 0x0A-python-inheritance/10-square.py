#!/usr/bin/python3
"""
contains a class and Raises
exception when required
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    inherits from rectangle
    """
    def __init__(self, size):
        """
        instantiation
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
