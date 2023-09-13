#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_dict = \
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_num = 0
    for item in range(len(roman_string)):
        if item > 0 and roman_dict[roman_string[item]] > \
           roman_dict[roman_string[item - 1]]:
            roman_num += roman_dict[roman_string[item]] - 2 * \
                roman_dict[roman_string[item - 1]]
        else:
            roman_num += roman_dict[roman_string[item]]
    return roman_num
