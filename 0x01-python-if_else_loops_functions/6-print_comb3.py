#!/usr/bin/python3
for first in range(9):
    for second in range(10):
        if first < second:
            print("{}{}".format(first, second), end=", ")
