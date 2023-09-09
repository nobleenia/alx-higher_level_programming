#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        biggest = my_list[0]
        for item in my_list:
            if item > biggest:
                biggest = item
    return biggest
