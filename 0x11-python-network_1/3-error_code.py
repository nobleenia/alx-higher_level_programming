#!/usr/bin/python3
"""
Script that takes in a URL,
Sends a request to the URL
Displays the body of the response (decoded in utf-8)
"""
import urllib.error
import urllib.request
from sys import argv


def main(argv):
    """
    Manages urllib.error.HTTPError exceptions
    """
    url = argv[1]
    quest = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(quest) as response:
            feedback = response.read()
            feed = feedback.decode("utf8")
            print(feed)
    except urllib.error.URLError as err:
        print("Error code: {}".format(err.code))


if __name__ == "__main__":
    main(argv)
