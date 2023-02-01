#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:05:14 2023
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
        """
        self.__height = height
        self.__width = width

    def __str__(self):
        """str method to print rectangle"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string

        for i in range(self.__height):
            for j in range(self.__width):
                string += '#'
            if i < self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """provides __repr__ method for object rectangle"""
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"

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
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
