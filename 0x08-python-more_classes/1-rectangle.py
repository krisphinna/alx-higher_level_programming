#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 14:04:30 2023
@author: Kris Adelowo
"""


class Rectangle:
    """class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Init method for Rectangle
        Attributes:
            width (int, optional): The width of the rectangle
            height (int, optional): The height of the rectangle
        self.width = width
        self.height = height
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """height property of the rectangle"""
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
        """width property of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
