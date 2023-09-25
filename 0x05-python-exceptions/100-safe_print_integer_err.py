#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
        return True
    except Exception as exc:
        print("Exception: {}".format(exc), file = stderr)
        return False
