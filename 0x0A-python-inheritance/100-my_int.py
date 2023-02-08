#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 15:13:37 2023
@author: Robinson Montes
"""


class MyInt(int):
    """A class that inherits from int"""
    def __eq__(self, num):
        """equal function for MyInt class"""
        return (int(self) != num)

    def __ne__(self, num):
        """no equal function for MyInt class"""
        return (int(self) == num)
