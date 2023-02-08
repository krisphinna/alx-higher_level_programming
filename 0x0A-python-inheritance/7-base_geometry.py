#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Web Feb 07 15:13:37 2023
@author: Robinson Montes
"""


class BaseGeometry():
    """An empty class"""
    pass

    def area(self):
        """Public instance method that calculates the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates integer input"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
