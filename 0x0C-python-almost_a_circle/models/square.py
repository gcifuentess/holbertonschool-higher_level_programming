#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class as a subclass of Rectangle"""

    symbol = '#'
    '''symbol used to print the square'''

    def __init__(self, size, x=0, y=0, id=None):
        """Square constructor"""
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """returns the string to be printed when print() invoked"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """Updates Square's attributes (id, size, x and y)"""
        i = 0
        for arg in args:
            i += 1
            if i == 1:
                self.id = arg
            elif i == 2:
                self.size = arg
            elif i == 3:
                self.x = arg
            elif i == 4:
                self.y = arg
            else:
                break
        if i == 0:
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                elif key == 'id':
                    self.id = value
                else:
                    break

    def to_dictionary(self):
        """retunrs a dictionary with the attributes of the class"""
        self.new_dict = {}
        self.new_dict['size'] = self.size
        self.new_dict['x'] = self.x
        self.new_dict['y'] = self.y
        self.new_dict['id'] = self.id
        return self.new_dict
