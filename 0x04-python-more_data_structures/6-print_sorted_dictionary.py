#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
   if a_dictionary is not None:
       [print("{}: {}".format(key, a_dictionary[key]))
               for key in sorted(a_dictionary)]
    #sorted_keys = sorted(a_dictionary.keys())
    #for k in sorted_keys:
        #print("{:s}: {}".format(k, a_dictionary[k]))
