#!/usr/bin/python3
"""
contains a class and Raises
exception when required
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    private height and width
    """
    def __init__(self, width, height):
        """
        instantiation
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
