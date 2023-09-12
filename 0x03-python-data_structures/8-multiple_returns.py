#!/usr/bin/python3
def multiple_returns(sentence):
    item_1 = len(sentence)
    if item_1 == 0:
        item_2 = None
    else:
        item_2 = sentence[0]

    return (item_1, item_2)
