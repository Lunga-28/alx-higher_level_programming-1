#!/usr/bin/python3
"""
contains a class and Raises
exception when required
"""

class BaseGeometry:
    """
    class has public instances
    """
    def area(self):
        """
        raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

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

    def area(self):
        """
        returns area of a rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        rectangle
        """
        return("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

class Square(Rectangle):
    """
    inherits from rectangle
    """
    def __init__(self, size):
        """
        class instantiation
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        function returns area of square
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        square
        """
        return("[Square] {:d}/{:d}".format(self.__size, self.__size))
