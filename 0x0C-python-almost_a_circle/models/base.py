#!/usr/bin/python3
"""Base Module"""
import json
import os.path


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base constructor"""
        if id is None:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if (list_dictionaries is None or not list_dictionaries):
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        if (list_objs is None or
                list_objs == [] or
                type(list_objs) is not list):
            json_str = json.dumps([])
        else:
            list_dicts = []
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
            json_str = Base.to_json_string(list_dicts)
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""

        if (json_string is None or
                type(json_string) is not str):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        else:
            return
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a JSON file"""
        if os.path.isfile(cls.__name__ + ".json") is False:
            return []
        lists = []
        instances = []
        with open(cls.__name__ + ".json", 'r') as f:
            for line in f:
                lists.append(Base.from_json_string(line))
        for a_list in lists:
            for dic in a_list:
                instances.append(cls.create(**dic))
        return instances
