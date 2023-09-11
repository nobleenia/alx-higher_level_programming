#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[:2]
    b = tuple_b[:2]

    if len(a) == 0:
        a += (0, 0)
    elif len(a) == 1:
        a += (0,)

    if len(b) == 0:
        b += (0, 0)
    elif len(b) == 1:
        b += (0,)

    result = (a[0] + b[0], a[1] + b[1])
    return result
