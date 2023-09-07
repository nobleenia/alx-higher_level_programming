#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argv_len = len(argv)
    if argv_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operands = {"+": add, "-": sub, "*": mul, "/": div}
    operator = argv[2]
    if operator not in operands:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, operands[operator](a, b)))
