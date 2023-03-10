#!/usr/bin/python3
# 0-rectangle.py
# Julius Okeyo <jaykopiyo@gmail.com>
'''
Class Rectangle
'''

class Rectangle:
    '''
    Class Rectangle with class attributes width and height
    '''
    def __init__(self, width = 0, height = 0):
        '''
        Initializing instance of class Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        '''

        self.width = width
        self.height = height
    
    @property
    def width(self):
        '''
        Method width for retrieving width
        '''

        return self.__width
    
    @width.setter
    def width(self, value):
        '''
        Method width for setting width
        '''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
        Method height for retrieving width
        '''

        return self.__height

    @height.setter
    def height(self, value):
        '''
        Method height for setting height
        '''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
