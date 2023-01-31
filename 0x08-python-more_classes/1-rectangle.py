#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue January 31 2023
@author: Kris Adelowo
"""


class Rectangle:
    """class of Rectangle that defines a rectangle"""

    def __init__(self, height=0, width=0,):
        """
        Init method for Rectangle

        Attributes:
            height (int, optional): The height of the rectangle
            width (int, optional): The width of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """set height property of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """set width property of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
