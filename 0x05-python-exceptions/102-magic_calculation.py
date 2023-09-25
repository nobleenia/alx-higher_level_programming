#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0;
    for in range(1, 4):
        try:
            if i > a:
                raise Exception('Too far')
            result = a ** b / i
        except Exception:
            result += b + a
    return result
