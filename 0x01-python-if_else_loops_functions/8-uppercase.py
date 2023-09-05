#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if char >= 'a' and char <= 'z':
            char = chr(ord(char) - ord('a') + ord('A'))
        print("{:s}".format(char), end="")
    print()
