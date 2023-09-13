#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for item in a_dictionary:
            if item == key:
                a_dictionary[item] = value
    return a_dictionary
