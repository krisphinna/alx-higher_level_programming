#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thur Feb 09 15:13:37 2023
@author: Robinson Montes
"""


def append_write(filename="", text=""):
    """Appends inputed text into a utf-8 encoded text file"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
