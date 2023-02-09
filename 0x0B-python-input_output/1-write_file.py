#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thru Feb 09 15:13:37 2023
@author: Robinson Montes
"""


def write_file(filename="", text=""):
    """
    write string to a file and return number of characters written
    """
    with open(filename, "w", encoding="UTF-8") as f:
        nc = f.write(text)

    return nc
