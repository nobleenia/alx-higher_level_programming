#!/usr/bin/python3
"""
Script that takes in a URL,
Sends a request to the URL,
Display value of X-Request-Id
"""
from sys import argv
import requests


def main(argv):
    """
    Displays the value of the X-Request-Id variable
    """
    url = argv[1]
    quest = requests.get(url)
    header = quest.headers.get("X-Request-Id")
    print(header)


if __name__ == "__main__":
    main(argv)
