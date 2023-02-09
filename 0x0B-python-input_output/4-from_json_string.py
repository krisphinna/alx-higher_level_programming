#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thru Feb 09 15:13:37 2023
@author: Robinson Montes
"""
import json


def from_json_string(my_str):
    """Convert a json string to a python object"""
    return json.loads(my_str)
