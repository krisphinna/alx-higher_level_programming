#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thru Feb 09 15:13:37 2023
@author: Robinson Montes
"""
import json


def to_json_string(my_obj):
    """Returs a json string containing object's representation"""
    return json.dumps(my_obj)
