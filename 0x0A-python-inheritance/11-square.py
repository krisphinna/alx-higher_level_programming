#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 15:13:37 2023
@author: Robinson Montes
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """A Square class shape, inheirts from BaseGeometry"""
    def __init__(self, size):
        """"Init function for Square"""
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """str funtion to print with/height"""
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """A function that calculates the area of the Square"""
        return self.__size ** 2
