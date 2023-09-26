#!/usr/bin/python3

from sys import stderr

def safe_function(fct, *args):
    try:
        output = fct(*args)
        return output
    except Exception as e:
        print("Exception: {}".format(e), file=stderr)
        return None
