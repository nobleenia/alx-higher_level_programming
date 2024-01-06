#!/usr/bin/python3
"""
Script that takes in a URL and an email address,
Sends a POST request to the passed URL with email as a parameter,
Displays the body of the response
"""
from sys import argv
import requests


def main(argv):
    """
    POST request to the passed URL with the email as a parameter
    """
    url = argv[1]
    var = {"email": argv[2]}
    quest = requests.post(url, data=var)
    print(quest.text)

if __name__ == "__main__":
    main(argv)
