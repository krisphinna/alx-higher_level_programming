#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:43:09 2023
@author: Kris
"""
import json


class Base:
   """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a json string representation"""
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the json string repressentation list object to a file
        """
        file_name = cls.__name__ + ".json"
        string = []
        if list_objs is not None:
            for i in list_objs:
                string.append(cls.to_dictionary(i))
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(string))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of json string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        file_name = cls.__name__ + ".json"
        json_obj = []
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                json_obj = cls.from_json_string(file.read())
            for key, value in enumerate(json_obj):
                json_obj[key] = cls.create(**json_obj[key])
        except:
            pass
        return json_obj
