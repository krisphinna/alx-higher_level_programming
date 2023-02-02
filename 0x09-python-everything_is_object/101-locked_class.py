#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 14:05:14 2023
@author: Kris Adelowo
"""


class LockedClass:
    """A locked class that only lets the user dynamically create the instance
        attribute 'first_name'"""
    __slots__ = ['first_name']
