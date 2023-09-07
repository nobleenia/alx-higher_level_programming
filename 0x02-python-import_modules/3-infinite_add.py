#!/usr/bin/python3
from sys import argv
sum = 0

if __name__ == "__main__":
    for item in argv:
        if argv.index(item) == 0:
            continue
        sum += int(item)

    print(sum)
