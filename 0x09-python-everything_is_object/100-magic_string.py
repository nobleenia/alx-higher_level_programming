#!/usr/bin/python3
def magic_string(n=[0]):
    n[0] += 1
    return str("BestSchool, " * (n[0] - 1)) + "BestSchool"
