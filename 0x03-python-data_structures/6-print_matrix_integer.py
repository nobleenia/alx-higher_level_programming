#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in matrix:
            for item in row:
                if row.index(item) != len(row) - 1:
                    last_char = " "
                else:
                    last_char = ""
                print("{:d}".format(item), end=last_char)
            print()
