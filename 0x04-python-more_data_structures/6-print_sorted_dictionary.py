#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    [print("{:s}: {}".format(key, a_dictionary[key])) 
            for key in sorted(a_dictionary)]
