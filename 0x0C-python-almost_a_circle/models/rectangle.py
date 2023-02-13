#!/usr/bin/python3
'''
Defines class Rectangle that inherits class Base
'''
from base import Base
class Rectangle(Base):
    '''
    Class Rectangle with private instance attributes
    __width -> width

    __height -> height

    __x -> x

    __y -> y
    each with its own public getter and setter.
    Class constructor: def __init__(self, width, height, x=0, y=0, id=None):

    Call the super class with id - this super call with use the logic of the __init__ of the Base class

    Assign each argument width, height, x and y to the right attribute.
    '''
    def __init__(self, width, height, x = 0, y = 0, id = None):
        '''
        Class constructor for class Rectangle
        Args:
            width - width of rectangle
            height - height of rectangle
            x - x displacement on x axis
            y - y displacement on y axis
        '''
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        '''
        Gets width
        '''
        return self.__width

    @width.setter
    def width(self, width):
        '''
        Sets width
        '''
        if (width is not int):
            raise TypeError("width must be an integer")
        if (width <= 0):
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        '''
        Gets height
        '''
        return self.__height

    @height.setter
    def height(self, height):
        '''
        Sets height
        '''
        if (height is not int):
            raise TypeError("height must be an integer")
        if (height <= 0):
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        '''
        Gets x
        '''
        return self.__x

    @x.setter
    def x(self, x):
        '''
        Sets x
        '''
        if (x is not int):
            raise TypeError("x must be an integer")
        if (x < 0):
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        '''
        Gets y
        '''
        return self.__y

    @y.setter
    def y(self, y):
        '''
        Sets y
        '''
        if (y is not int):
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        '''
        Calculates the areas of a rectangle
        '''
        return (self.width * self.height)

    def display(self):
        '''
        Displays a rectangle using # characters
        '''
        [print("") for y in range(self.y)] #Adjusts the position of rectangle on y axis
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)] #Adjusts the position of the rectangle on the x axis
            for j in range(self.width):
                print("{}".format("#"))
            if (i != self.height - 1):
                print("\n")

    def update(self, *args, **kwargs):
        '''
        Updates class attributes with passed arguments
         Args:
            *args (ints): New attribute values.
            - 1st argument represents id attribute
            - 2nd argument represents width attribute
            - 3rd argument represent height attribute
            - 4th argument represents x attribute
            - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        '''
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        Return the dictionary representation of the rectangle.
        """
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}
