#!/usr/bin/python3
"""
Script that takes in a URL,
Sends a request to the URL and
Displays the body of the response
"""
import requests
from sys import argv


def main(argv):
    """
    Method that manage urllib.error.HTTPError exceptions and
    print: Error code: followed by the HTTP status code
    """
    url = argv[1]
    quest = requests.get(url)
    if quest.status_code == requests.codes.ok:
        print(quest.text)
    else:
        print("Error code: {}".format(quest.status_code))


if __name__ == "__main__":
    main(argv)
