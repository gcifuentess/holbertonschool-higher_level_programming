#!/usr/bin/python3
"""Student to JSON module"""


class Student():
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Student constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Returns dictionary description of json object filtered'''
        flag = False
        if (type(attrs) is list):
            flag = True
            for attr in attrs:
                if type(attr) is not str:
                    flag = False
        if flag is True:
            my_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    my_dict[key] = value
        else:
            my_dict = self.__dict__.copy()

        return my_dict

    def reload_from_json(self, json):
        """Updates attributes with json"""

        for key, value in json.items():
            self.__dict__[key] = value
