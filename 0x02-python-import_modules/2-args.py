#!/usr/bin/python3
from sys import argv

argv_len = len(argv) - 1

if __name__ == "__main__":
    if argv_len == 0:
        print(f"{argv_len:d} arguments.")
    elif argv_len == 1:
        print(f"{argv_len:d} argument:")
    else:
        print(f"{argv_len:d} arguments:")

for item in argv:
    if argv.index(item) == 0:
        continue
    print(f"{argv.index(item):d}: {item:s}")
