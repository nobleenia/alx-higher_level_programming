#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5

if __name__ == "__main__":
    print(f"{a:d} + {b:d} = {add(a, b):d}")
    print(f"{a:d} - {b:d} = {sub(a, b):d}")
    print(f"{a:d} * {b:d} = {mul(a, b):d}")
    print(f"{a:d} / {b:d} = {div(a, b):d}")
