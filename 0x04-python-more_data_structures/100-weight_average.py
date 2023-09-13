#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    avg = 0
    div = 0

    for tupls in my_list:
        avg += (tupls[0] * tupls[1])
        div += tupls[1]
    return float(avg / div)
