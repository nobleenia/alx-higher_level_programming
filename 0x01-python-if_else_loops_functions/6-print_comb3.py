#!/usr/bin/python3
for first in range(9):
    for second in range(10):
        if first < second:
            if first == 8 and second == 9:
                print("{}{}".format(first, second))
            else:
                print("{}{}".format(first, second), end=", ")
