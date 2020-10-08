#!/usr/bin/python3
"""Student to JSON module"""


class Student():
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Student constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Returns dictionary description of json object.'''
        if hasattr(self, "__dict__"):
            return self.__dict__.copy()
        else:
            return {}
