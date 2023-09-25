#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_items = 0
    for index in range(x):
        try:
            print(my_list[index], end="")
            num_items += 1
        except IndexError:
            break
    print()
    return num_items
