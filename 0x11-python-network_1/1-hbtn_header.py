#!/usr/bin/python3
"""
Script takes and sends a request to the URL
and displays value of X-Request-Id var in header
"""
import urllib.request
from sys import argv


def main(argv):
    """
    Takes and requests a url of the X-Request-Id var
    """
    url = argv
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        req_id = headers["X-Request-Id"]
        print(req_id)


if __name__ == "__main__":
    main(argv[1])
