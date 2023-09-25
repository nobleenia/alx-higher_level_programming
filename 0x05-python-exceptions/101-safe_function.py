#!/usr/bin/python3
from sys import stderr
def safe_function(fct, *args):
    try:
        output = fct(*args)
        return output
    except Exception as exc:
        print("Exception: {}".format(exc), file = stderr)
        return None
