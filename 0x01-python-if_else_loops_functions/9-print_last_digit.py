#!/usr/bin/python3
def print_last_digit(number):
    abs_num = abs(number)
    num = abs_num % 10
    print(f"{num}", end="")
    return num
