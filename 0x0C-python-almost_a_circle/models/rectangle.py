#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle, a subclass of class Base"""

    symbol = '#'
    '''symbol used to print the rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value < 1:
                raise ValueError("width must be > 0")
            self.__width = int(value)
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value < 1:
                raise ValueError("height must be > 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """returns the area of the rectangle instance"""
        return self.width * self.height

    def display(self):
        '''prints the rectangle instance'''
        if not self.__width or not self.__height:
            self.__str_print = ""
        # x offset:
        self.__str_line = (str(" " * self.__x) +
                           str(self.symbol * self.__width) + '\n')

        # y offset:
        self.__str_print = (str('\n' * self.__y) +
                            self.__str_line * self.__height)[:-1]
        print(self.__str_print)

    def __str__(self):
        """returns the string to be printed when print() invoked"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """Updates Reactangle's attributes (id, width, height, x and y)"""
        i = 0
        for arg in args:
            i += 1
            if i == 1:
                self.id = arg
            elif i == 2:
                self.width = arg
            elif i == 3:
                self.height = arg
            elif i == 4:
                self.x = arg
            elif i == 5:
                self.y = arg
            else:
                break
        if i == 0:
            for key, value in kwargs.items():
                if key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
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
        self.new_dict['width'] = self.__width
        self.new_dict['height'] = self.__height
        self.new_dict['x'] = self.__x
        self.new_dict['y'] = self.__y
        self.new_dict['id'] = self.id
        return self.new_dict
