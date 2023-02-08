#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 15:13:37 2023
@author: Robinson Montes
"""


def is_same_class(obj, a_class):
    """Checks if two objects are the same class"""
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    return (type(obj) is a_class)
