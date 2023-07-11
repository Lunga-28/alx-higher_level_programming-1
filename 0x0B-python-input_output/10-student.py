#!/usr/bin/python3
"""
class with public attributes
"""


class Student:
    """
    public instances
    """
  
    def __init__(self, first_name, last_name, age):
        """
        instantiation
        """
      
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns dict repres instance
        """
      
        if attrs is None:
            return (self.__dict__)
        return ({key: value for key, value in self.__dict__.items()
                 if key in attrs})
