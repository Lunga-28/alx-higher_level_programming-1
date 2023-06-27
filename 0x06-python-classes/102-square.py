#!/usr/bin/python3

"""Define a Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int or float): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int or float): The new size of the square.

        Raises:
            TypeError: If the value is not a number (float or integer).
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare if two squares are equal in terms of area."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """Compare if two squares are not equal in terms of area."""
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __lt__(self, other):
        """Compare if the area of the square is less than the other square."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Compare if the area of the square is less than or equal to the other square."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """Compare if the area of the square is greater than the other square."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """Compare if the area of the square is greater than or equal to the other square."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
