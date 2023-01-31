#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue January 31 2023
@author: Kris Adelowo
"""


class Rectangle:
    """class of Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0,):
        """
        Init method for Rectangle

        Attributes:
            width (int, optional): The width of the rectangle
            height (int, optional): The height of the rectangle
        """
        self.__width = width
        self.__height = height

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

    @property
    def height(self):
        """set height property of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
