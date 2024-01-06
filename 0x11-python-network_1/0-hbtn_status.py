#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


def main():
    """
    Prints response from https://alx-intranet.hbtn.io/status
    """
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        feedback = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(feedback)))
        print("\t- content: {}".format(feedback))
        print("\t- utf8 content: {}".format(feedback.decode("utf8")))

if __name__ == "__main__":
    main()
