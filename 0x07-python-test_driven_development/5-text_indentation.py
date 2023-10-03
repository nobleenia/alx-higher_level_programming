#!/usr/bin/python3
"""
text_indentation
Module defines a function for formatting text by adding newlines after certain punctuation marks
"""


def text_indentation(text):
    """
    Format text by adding newlines after certain punctuation marks.

    Args:
        text (str): The input text to be formatted.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")

    list_lines = [line.strip() for line in text.split('\n')]

    print("\n".join(list_lines), end="")
